import ctypes
from . import alc
from . import al
from .exceptions import OalError

def get_default_capture_device():
    """
    Returns the specifier for the default audio capture (input) device.

    Returns:
        str: The name of the default capture device.
    """
    ptr = alc.alcGetString(None, alc.ALC_CAPTURE_DEFAULT_DEVICE_SPECIFIER)
    if not ptr:
        return ""
    return ctypes.string_at(ptr).decode('utf-8')

def get_available_capture_devices():
    """
    Returns a list of specifiers for all available audio capture devices.

    Returns:
        list[str]: A list of names of available capture devices.
    """
    ptr = alc.alcGetString(None, alc.ALC_CAPTURE_DEVICE_SPECIFIER)
    if not ptr:
        return []

    devices = []
    offset = 0
    while True:
        current_device_bytes = ctypes.string_at(ptr + offset)
        if not current_device_bytes:
            break
        devices.append(current_device_bytes.decode('utf-8'))
        offset += len(current_device_bytes) + 1
        
    return devices


class CaptureDevice:
    """Represents a physical audio capture (input) device."""

    def __init__(self, device_name=None, frequency=44100, audio_format=al.AL_FORMAT_MONO16, buffer_size=4096):
        """
        Opens a capture device.

        Args:
            device_name (str, optional): The name of the device to open. Defaults to the system default.
            frequency (int, optional): The sample rate to capture at. Defaults to 44100.
            audio_format (int, optional): The format to capture in (e.g., CaptureFormat.MONO_16). Defaults to 16-bit mono.
            buffer_size (int, optional): The size of the internal ring buffer, in samples. Defaults to 4096.
        """
        if device_name and not isinstance(device_name, bytes):
            device_name = device_name.encode('utf-8')

        self._device = alc.alcCaptureOpenDevice(device_name, frequency, audio_format, buffer_size)
        if not self._device:
            raise OalError("Could not open capture device")
        
        self.format = audio_format
        self.frequency = frequency

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        """Closes the capture device."""
        if self._device:
            self.stop()
            alc.alcCaptureCloseDevice(self._device)
            self._device = None

    def start(self):
        """Starts capturing audio."""
        alc.alcCaptureStart(self._device)
    
    def stop(self):
        """Stops capturing audio. Captured samples remain available to be read."""
        if self._device:
            alc.alcCaptureStop(self._device)

    @property
    def available_samples(self):
        """The number of samples currently available to be read from the internal buffer."""
        num_samples = ctypes.c_int(0)
        alc.alcGetIntegerv(self._device, alc.ALC_CAPTURE_SAMPLES, 1, ctypes.byref(num_samples))
        return num_samples.value

    def capture_samples(self, num_samples):
        """
        Reads a number of samples from the device's internal buffer.

        Args:
            num_samples (int): The maximum number of samples to read.

        Returns:
            bytes: The raw audio data of the captured samples.
        """
        if num_samples == 0:
            return b''
            
        buffer = (ctypes.c_byte * num_samples)()
        alc.alcCaptureSamples(self._device, ctypes.byref(buffer), num_samples)
        return buffer.raw
