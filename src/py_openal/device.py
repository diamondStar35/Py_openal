import ctypes
from . import alc
from .exceptions import OalError
from .enums import HrtfStatus, HrtfMode, OutputMode, ChannelLayout

_device_ext_procs = {}

def get_default_device():
    """
    Returns the specifier for the default audio output device.

    Returns:
        str: The name of the default device.
    """
    ptr = alc.alcGetString(None, alc.ALC_DEFAULT_DEVICE_SPECIFIER)
    if not ptr:
        return ""
    specifier_bytes = ctypes.string_at(ptr)
    return specifier_bytes.decode('utf-8')

def get_available_devices():
    """
    Returns a list of specifiers for all available audio output devices.

    This relies on the ALC_ENUMERATE_ALL_EXT extension.

    Returns:
        list[str]: A list of names of available devices.
    """
    if not alc.alcIsExtensionPresent(None, b"ALC_ENUMERATE_ALL_EXT"):
        return [get_default_device()]
        
    ptr = alc.alcGetString(None, alc.ALC_ALL_DEVICES_SPECIFIER)
    if not ptr:
        return []

    devices = []
    offset = 0
    while True:
        # ptr is an address (integer), so ptr + offset is valid pointer arithmetic
        current_device_bytes = ctypes.string_at(ptr + offset)
        # An empty string means we've hit the double-null terminator
        if not current_device_bytes:
            break
        devices.append(current_device_bytes.decode('utf-8'))
        offset += len(current_device_bytes) + 1
        
    return devices


class Device:
    """Represents a physical audio device."""
    def __init__(self, device_specifier=None, **attributes):
        """
        Opens a device, optionally with specific attributes.
        
        Note: Opening a device with attributes requires resetting it immediately
        after opening, which is a feature of the ALC_SOFT_device_reset extension.
        
        Args:
            device_specifier (str, optional): A specific device name, or None for the default.
            **attributes: Keyword arguments for device configuration. These are
                          the same as the ones for the Context constructor.
                          Using `hrtf=True` will automatically request a stereo
                          output format compatible with HRTF.
        """
        if device_specifier and not isinstance(device_specifier, bytes):
            device_specifier = device_specifier.encode('utf-8')
            
        self._device = alc.alcOpenDevice(device_specifier)
        if not self._device:
            raise OalError("Could not open device")
        
        self._as_parameter_ = self._device

        if attributes:
            # If HRTF is requested, we must also ensure a stereo format is requested
            # to avoid the UNSUPPORTED_FORMAT error. We add it to the attributes dict.
            hrtf_request = attributes.get('hrtf')
            if hrtf_request is True or hrtf_request == HrtfMode.ENABLED:
                attributes['output_mode'] = OutputMode.STEREO_HRTF

            # We need to import the builder function here to avoid circular dependencies
            from .context import _build_attribute_list
            attr_list = _build_attribute_list(attributes)
            if not self.reset(attr_list):
                # If reset fails, close the device to prevent leaving it in a bad state
                self.close()
                raise OalError("Failed to reset device with specified attributes.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        """Closes the device."""
        if self._device:
            if not alc.alcCloseDevice(self._device):
                raise OalError("Failed to close device")
            self._device = None

    def _get_ext_proc(self, func_name, argtypes, restype):
        """Internal helper to load and cache ALC extension functions for this device."""
        if func_name in _device_ext_procs:
            return _device_ext_procs[func_name]
        
        # alcGetProcAddress requires a device handle to look up ALC extensions
        func_ptr = alc.alcGetProcAddress(self._device, func_name.encode('utf-8'))
        if not func_ptr:
            raise OalError(f"ALC extension function '{func_name}' not supported by this device.")
            
        cfunc = ctypes.CFUNCTYPE(restype, *argtypes)(func_ptr)
        # We don't set errcheck here because we'll call the function directly
        _device_ext_procs[func_name] = cfunc
        return cfunc

    def pause(self):
        """
        Pauses all processing on this device.
        
        This releases the underlying audio hardware for other applications
        and pauses all contexts associated with this device.
        """
        if self.is_closed:
            raise OalError("Device is closed.")
        
        # Dynamically get the function pointer
        proc = self._get_ext_proc('alcDevicePauseSOFT', [ctypes.c_void_p], None)
        proc(self._device)
        # We don't need alc_check_error here because the raw call doesn't use it,
        # but errors will still be raised by the underlying driver if needed.
        # To be fully correct, we should check the error manually.
        err = alc.alcGetError(self._device)
        if err != alc.ALC_NO_ERROR:
            raise OalError("Error pausing device.") # A more specific error could be looked up

    def resume(self):
        """
        Resumes processing on a paused device.
        
        This will attempt a simple resume first. If that fails, it will
        fall back to reopening the device to ensure a robust recovery.
        """
        if self.is_closed:
            raise OalError("Device is closed.")
            
        proc = self._get_ext_proc('alcDeviceResumeSOFT', [ctypes.c_void_p], None)
        proc(self._device)
        
        err = alc.alcGetError(self._device)
        if err != alc.ALC_NO_ERROR:
            # The simple resume failed. This can happen on some backends.
            # Fall back to the more robust reopen() method to recover.
            # We pass None to reopen the current device with its existing attributes.
            reopen_success = self.reopen(None, None)
            if not reopen_success:
                try:
                    error_name = alc.alc_enums[err][0]
                    raise OalError(f"Error resuming device ({error_name}). Reopen fallback also failed.")
                except (KeyError, IndexError):
                    raise OalError(f"Error resuming device (code: {err}). Reopen fallback also failed.")

    def reset(self, attributes=None):
        """
        Resets the device with a new set of attributes.

        This can be used to change device properties like output frequency,
        HRTF mode, etc., on the fly without destroying existing contexts.
        This requires the ALC_SOFT_device_reset extension.

        Args:
            attributes (list, optional): A C-style list of integer attributes,
                                         e.g., [alc.ALC_FREQUENCY, 48000, 0].
                                         The list must be null-terminated (end with 0).
                                         If None, resets with default attributes.
        
        Returns:
            bool: True on success, False on failure.
        """
        if self.is_closed:
            raise OalError("Device is closed.")

        proc = self._get_ext_proc(
            'alcResetDeviceSOFT',
            [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)],
            ctypes.c_uint8 # ALCboolean
        )

        attr_array = None
        if attributes:
            if not attributes or attributes[-1] != 0:
                raise ValueError("Attribute list must be terminated with a 0.")
            attr_array = (ctypes.c_int * len(attributes))(*attributes)
            
        result = proc(self._device, attr_array)
        err = alc.alcGetError(self._device)
        if err != alc.ALC_NO_ERROR:
            raise OalError("Error resetting device.")

        return bool(result)

    def reopen(self, device_specifier=None, attributes=None):
        """
        Reopens the device with a new specifier and/or attributes.
        
        This can be used to switch to a new output device on the fly
        without destroying the existing contexts.
        
        Args:
            device_specifier (str, optional): The name of the new device to open.
                                              If None, reopens the current device.
            attributes (list, optional): A list of new context attributes,
                                         e.g., [alc.ALC_HRTF_SOFT, alc.ALC_TRUE, 0].
        
        Returns:
            bool: True on success, False on failure.
        """
        if self.is_closed:
            raise OalError("Device is closed.")
        
        proc = self._get_ext_proc(
            'alcReopenDeviceSOFT',
            [ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)],
            ctypes.c_uint8 # ALCboolean
        )
            
        spec_bytes = None
        if device_specifier:
            if not isinstance(device_specifier, bytes):
                spec_bytes = device_specifier.encode('utf-8')
            else:
                spec_bytes = device_specifier

        attr_array = None
        if attributes:
            attr_array = (ctypes.c_int * len(attributes))(*attributes)

        result = proc(self._device, spec_bytes, attr_array)
        err = alc.alcGetError(self._device)
        if err != alc.ALC_NO_ERROR:
            raise OalError("Error reopening device.")
            
        return bool(result)

    def is_extension_present(self, ext_name: str) -> bool:
        """
        Checks if a specific ALC extension is supported by this device.

        Args:
            ext_name (str): The name of the extension to check (e.g., "ALC_SOFT_HRTF").

        Returns:
            bool: True if the extension is present, False otherwise.
        """
        if self.is_closed:
            raise OalError("Device is closed.")
        
        if not isinstance(ext_name, bytes):
            ext_name_bytes = ext_name.encode('utf-8')
        else:
            ext_name_bytes = ext_name
            
        return bool(alc.alcIsExtensionPresent(self._device, ext_name_bytes))

    def get_clock(self) -> dict:
        """
        Gets the current device clock time and latency.
        This requires the ALC_SOFT_device_clock extension.

        The clock is a high-precision, monotonically increasing value in nanoseconds.
        It is suitable for scheduling and synchronization.

        Returns:
            dict: A dictionary with 'clock' (int, ns) and 'latency' (int, ns) keys.
        """
        if self.is_closed:
            raise OalError("Device is closed.")

        # The C function takes a pointer to an array of two 64-bit integers.
        values = (alc.ALCint64SOFT * 2)()        
        proc = self._get_ext_proc('alcGetInteger64vSOFT', [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.POINTER(alc.ALCint64SOFT)], None)        
        proc(self._device, alc.ALC_DEVICE_CLOCK_LATENCY_SOFT, 2, values)
        
        err = alc.alcGetError(self._device)
        if err != alc.ALC_NO_ERROR:
            raise OalError("Error getting device clock.")
            
        return {'clock': values[0], 'latency': values[1]}

    @property
    def specifier(self):
        """The specifier string for this specific device."""
        if self.is_closed:
            raise OalError("Device is closed.")
        ptr = alc.alcGetString(self._device, alc.ALC_DEVICE_SPECIFIER)
        return ctypes.string_at(ptr).decode('utf-8') if ptr else ""

    @property
    def alc_version(self):
        """
        The ALC version supported by this device.
        
        Returns:
            tuple[int, int]: A tuple containing the (major, minor) version numbers.
        """
        if self.is_closed:
            raise OalError("Device is closed.")
        major = ctypes.c_int()
        minor = ctypes.c_int()
        alc.alcGetIntegerv(self._device, alc.ALC_MAJOR_VERSION, 1, ctypes.byref(major))
        alc.alcGetIntegerv(self._device, alc.ALC_MINOR_VERSION, 1, ctypes.byref(minor))
        return (major.value, minor.value)

    @property
    def extensions(self):
        """A list of ALC extensions supported by this specific device."""
        if self.is_closed:
            raise OalError("Device is closed.")
        ptr = alc.alcGetString(self._device, alc.ALC_EXTENSIONS)
        if not ptr:
            return []
        extensions_str = ctypes.string_at(ptr).decode('utf-8')
        return extensions_str.split(' ')

    @property
    def hrtf_status(self) -> HrtfStatus:
        """
        The current HRTF status for this device.
        Requires the ALC_SOFT_HRTF extension.
                
        Returns:
            HrtfStatus: The current status of the HRTF renderer.
        """
        if self.is_closed:
            raise OalError("Device is closed.")
        
        status = ctypes.c_int(0)
        alc.alcGetIntegerv(self._device, alc.ALC_HRTF_STATUS_SOFT, 1, ctypes.byref(status))
        return HrtfStatus(status.value)

    @property
    def available_hrtfs(self) -> list[dict]:
        """
        A list of available HRTF profiles for this device.
        Requires the ALC_SOFT_HRTF extension.
        
        Returns:
            list[dict]: A list of dictionaries, where each dictionary has
                        'name' (str) and 'id' (int) keys for an HRTF profile.
                        Returns an empty list if none are found.
        """
        if self.is_closed:
            raise OalError("Device is closed.")

        num_hrtf = ctypes.c_int(0)
        alc.alcGetIntegerv(self._device, alc.ALC_NUM_HRTF_SPECIFIERS_SOFT, 1, ctypes.byref(num_hrtf))
        
        hrtf_list = []
        if num_hrtf.value > 0:
            for i in range(num_hrtf.value):
                hrtf_name = alc.alcGetStringiSOFT(self._device, alc.ALC_HRTF_SPECIFIER_SOFT, i)
                hrtf_list.append({'name': hrtf_name.decode('utf-8'), 'id': i})
        return hrtf_list

    @property
    def current_hrtf(self) -> str:
        """
        The name of the currently active HRTF profile.
        Requires the ALC_SOFT_HRTF extension.
        
        Returns:
            str: The name of the current HRTF profile, or an empty string
                 if HRTF is not enabled.
        """
        if self.is_closed:
            raise OalError("Device is closed.")

        if self.hrtf_status != HrtfStatus.ENABLED:
            return ""

        # The spec states that alcGetStringiSOFT with index 0 will return the
        # name of the currently enabled HRTF.
        hrtf_name = alc.alcGetStringiSOFT(self._device, alc.ALC_HRTF_SPECIFIER_SOFT, 0)
        return hrtf_name.decode('utf-8')

    @property
    def output_mode(self) -> OutputMode:
        """
        The current output mode of the device (e.g., Stereo, HRTF, 7.1 Surround).
        Requires the ALC_SOFT_output_mode extension.
        """
        if self.is_closed:
            raise OalError("Device is closed.")
        
        mode = ctypes.c_int(0)
        alc.alcGetIntegerv(self._device, alc.ALC_OUTPUT_MODE_SOFT, 1, ctypes.byref(mode))
        return OutputMode(mode.value)

    def init_hrtf(self, requested_hrtf=None):
        """
        Initializes HRTF on this device. The device will be reset.
        This requires the ALC_SOFT_HRTF extension.

        This method automatically requests a stereo output format, which is
        required for HRTF to function correctly.

        Args:
            requested_hrtf (str or int, optional): The name (str) or ID (int) of a
                                                   specific HRTF to use. If None,
                                                   the default is used.
        
        Returns:
            True if HRTF was successfully enabled.
        """
        if self.is_closed:
            raise OalError("Device is closed.")
            
        if not alc.alcIsExtensionPresent(self._device, b"ALC_SOFT_HRTF"):
            raise OalError("HRTF extension not present on this device.")

        attrs = {
            'format_channels': ChannelLayout.STEREO,
            'hrtf': HrtfMode.ENABLED,
            'output_mode': OutputMode.STEREO_HRTF,
        }

        if requested_hrtf is not None:
            hrtf_id = -1
            if isinstance(requested_hrtf, str):
                found = False
                for hrtf_profile in self.available_hrtfs:
                    if hrtf_profile['name'] == requested_hrtf:
                        hrtf_id = hrtf_profile['id']
                        found = True
                        break
                if not found:
                    raise OalError(f'HRTF profile name "{requested_hrtf}" not found.')
            elif isinstance(requested_hrtf, int):
                hrtf_id = requested_hrtf
            else:
                raise TypeError("requested_hrtf must be a string (name) or an integer (ID).")

            attrs['hrtf_id'] = hrtf_id
        
        from .context import _build_attribute_list
        attr_list = _build_attribute_list(attrs)
        
        if not self.reset(attr_list):
            raise OalError("Failed to reset device with HRTF attributes.")

        # Check if HRTF is now enabled
        hrtf_state = ctypes.c_int(0)
        alc.alcGetIntegerv(self._device, alc.ALC_HRTF_STATUS_SOFT, 1, ctypes.byref(hrtf_state))
        
        return hrtf_state.value == alc.ALC_TRUE

    @property
    def is_closed(self):
        return self._device is None

    @property
    def is_connected(self):
        """
        Checks if the audio device is still physically connected.
        This requires the ALC_EXT_disconnect extension.

        Returns:
            bool: True if the device is connected, False otherwise.
                  Returns False if the device has been closed via .close().
        """
        if self.is_closed:
            return False

        value = ctypes.c_int()
        # alcGetIntegerv will raise an ALCError (INVALID_ENUM) if the extension
        # is not supported, which is the desired behavior.
        alc.alcGetIntegerv(self._device, alc.ALC_CONNECTED, 1, ctypes.byref(value))
        return bool(value.value)
