import ctypes
from . import alc
from .exceptions import OalError
from .enums import ChannelLayout, SampleType

class LoopbackDevice:
    """
    Represents a loopback audio device for non-real-time rendering.

    This device does not play to a physical output. Instead, audio is rendered
    to an internal buffer and can be retrieved by calling render_samples().
    This requires the ALC_SOFT_loopback extension.
    """
    def __init__(self, device_name=None):
        """
        Opens a loopback device.

        Args:
            device_name (str, optional): The name of the playback device to
                                         base the loopback device on. If None,
                                         the system default is used.
        """
        if device_name and not isinstance(device_name, bytes):
            device_name = device_name.encode('utf-8')

        self._device = alc.alcLoopbackOpenDeviceSOFT(device_name)
        if not self._device:
            raise OalError("Could not open loopback device.")
        self._as_parameter_ = self._device

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        """Closes the loopback device."""
        if self._device:
            alc.alcCloseDevice(self._device)
            self._device = None

    @property
    def is_closed(self):
        """Returns True if the device has been closed."""
        return self._device is None

    def is_format_supported(self, frequency: int, channels: ChannelLayout, sample_type: SampleType) -> bool:
        """
        Checks if the device can render to a specific audio format.

        Args:
            frequency (int): The sample rate in Hz.
            channels (ChannelLayout): The desired channel layout.
            sample_type (SampleType): The desired sample type.

        Returns:
            bool: True if the format is supported, False otherwise.
        """
        if self.is_closed:
            raise OalError("Device is closed.")
        return bool(alc.alcIsRenderFormatSupportedSOFT(self._device, frequency, channels, sample_type))

    def render_samples(self, num_samples: int, frequency: int, channels: ChannelLayout, sample_type: SampleType) -> bytes:
        """
        Renders a block of audio and returns the raw sample data.

        This function must be called with a format that is supported by the
        device (see is_format_supported).

        Args:
            num_samples (int): The number of sample frames to render.
            frequency (int): The sample rate to render at.
            channels (ChannelLayout): The channel layout to render.
            sample_type (SampleType): The sample type to render.

        Returns:
            bytes: The raw audio data of the rendered samples.
        """
        if self.is_closed:
            raise OalError("Device is closed.")
        if num_samples == 0:
            return b''

        # Determine bytes per sample and channel count to calculate buffer size
        if sample_type in (SampleType.BYTE, SampleType.UNSIGNED_BYTE):
            bytes_per_sample = 1
        elif sample_type in (SampleType.SHORT, SampleType.UNSIGNED_SHORT):
            bytes_per_sample = 2
        elif sample_type in (SampleType.INT, SampleType.UNSIGNED_INT, SampleType.FLOAT):
            bytes_per_sample = 4
        elif sample_type == SampleType.DOUBLE:
            bytes_per_sample = 8
        else:
            raise TypeError(f"Invalid sample_type for rendering: {sample_type}")

        # Determine number of channels for the given layout
        if channels == ChannelLayout.MONO:
            num_channels = 1
        elif channels in (ChannelLayout.STEREO, ChannelLayout.REAR):
            num_channels = 2
        elif channels == ChannelLayout.QUAD:
            num_channels = 4
        elif channels == ChannelLayout.SURROUND_5_1:
            num_channels = 6
        elif channels == ChannelLayout.SURROUND_6_1:
            num_channels = 7
        elif channels == ChannelLayout.SURROUND_7_1:
            num_channels = 8
        else:
            raise TypeError(f"Invalid or unsupported channel layout for rendering: {channels}")

        buffer_size = num_samples * num_channels * bytes_per_sample
        if buffer_size == 0:
            return b''
            
        buffer = (ctypes.c_byte * buffer_size)()
        # The alcRenderSamplesSOFT function in OpenAL Soft currently only supports
        # mono and stereo rendering formats. We check this to provide a clear error.
        if channels not in (ChannelLayout.MONO, ChannelLayout.STEREO):
             if not self.is_format_supported(frequency, channels, sample_type):
                  raise OalError(f"The format with channel layout '{channels.name}' is not supported for rendering by the loopback device.")

        alc.alcRenderSamplesSOFT(self._device, ctypes.byref(buffer), num_samples)
        return buffer.raw

