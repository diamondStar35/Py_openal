import ctypes
from . import alc
from .exceptions import OalError

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
    def __init__(self, device_specifier=None):
        """
        Opens a device.
        
        Args:
            device_specifier: A specific device name, or None for the default.
        """
        if device_specifier and not isinstance(device_specifier, bytes):
            device_specifier = device_specifier.encode('utf-8')
            
        self._device = alc.alcOpenDevice(device_specifier)
        if not self._device:
            raise OalError("Could not open device")
        
        self._as_parameter_ = self._device

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

    def init_hrtf(self, requested_hrtf=None):
        """
        Initializes HRTF on this device. The device will be reset.
        This requires the ALC_SOFT_HRTF extension.

        Args:
            requested_hrtf (str, optional): The name of a specific HRTF to use.
                                            If None, the default is used.
        
        Returns:
            True if HRTF was successfully enabled.
        """
        if self.is_closed:
            raise OalError("Device is closed.")
            
        if not alc.alcIsExtensionPresent(self._device, b"ALC_SOFT_HRTF"):
            raise OalError("HRTF extension not present on this device.")

        num_hrtf = ctypes.c_int(0)
        alc.alcGetIntegerv(self._device, alc.ALC_NUM_HRTF_SPECIFIERS_SOFT, 1, ctypes.byref(num_hrtf))
        if num_hrtf.value == 0:
            raise OalError("No HRTFs found on this device.")

        attr = [alc.ALC_HRTF_SOFT, alc.ALC_TRUE]
        if requested_hrtf:
            found = False
            for i in range(num_hrtf.value):
                hrtf_name = alc.alcGetStringiSOFT(self._device, alc.ALC_HRTF_SPECIFIER_SOFT, i)
                if hrtf_name.decode('utf-8') == requested_hrtf:
                    attr.extend([alc.ALC_HRTF_ID_SOFT, i])
                    found = True
                    break
            if not found:
                raise OalError(f'HRTF "{requested_hrtf}" not found.')
        
        attr.append(0) # Null terminator
        attr_array = (ctypes.c_int * len(attr))(*attr)

        if not alc.alcResetDeviceSOFT(self._device, attr_array):
            raise OalError("Failed to reset device with HRTF attributes.")

        # Check if HRTF is now enabled
        hrtf_state = ctypes.c_int(0)
        alc.alcGetIntegerv(self._device, alc.ALC_HRTF_SOFT, 1, ctypes.byref(hrtf_state))
        
        return hrtf_state.value == alc.ALC_TRUE            

    @property
    def is_closed(self):
        return self._device is None
