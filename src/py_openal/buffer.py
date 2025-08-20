import ctypes
import warnings
from . import al
from .enums import ChannelLayout, SampleType, AudioFormat

class Buffer:
    """Represents an OpenAL buffer for storing audio data."""

    def __init__(self, data_format: AudioFormat, data, size, frequency):
        """
        Creates an OpenAL buffer and fills it with audio data.
        
        Args:
            data_format (AudioFormat): The format of the provided `data`.
            data (bytes): The raw audio data bytes.
            size (int): The size of the data in bytes.
            frequency (int): The sample rate of the audio in Hz.
        """
        self._id = ctypes.c_uint()
        al.alGenBuffers(1, ctypes.pointer(self._id))
        
        self._id_value = self._id.value
        
        al.alBufferData(self._id, data_format, data, size, frequency)

    def set_data(self, data_format, data, size, frequency):
        """
        Fills (or refills) the buffer with new audio data.

        This can be used to change the sound contained in this buffer.
        Warning: Do not call this while a source is actively playing this buffer.
        
        Args:
            data_format: The format of the data (e.g., al.AL_FORMAT_MONO16).
            data: The raw audio data bytes.
            size: The size of the data in bytes.
            frequency: The sample rate of the audio.
        """
        if self._id_value is None:
            raise OalError("Buffer has been destroyed.")
        al.alBufferData(self._id, data_format, data, size, frequency)

    def set_data_samples(self, samplerate: int, internal_format: AudioFormat, samples: bytes, channels: ChannelLayout, sample_type: SampleType):
        """
        Fills the buffer with new audio data using sample-based parameters.
        This is a more flexible alternative to set_data().
        Requires the AL_SOFT_buffer_samples extension.

        Args:
            samplerate (int): The sample rate of the audio in Hz.
            internal_format (AudioFormat): The destination format OpenAL should use for
                                           internal storage.
            samples (bytes): The raw audio data bytes.
            channels (ChannelLayout): The channel layout of the provided `samples` data.
            sample_type (SampleType): The data type of each individual sample in
                                      the `samples` data.
        """
        if self._id_value is None:
            raise OalError("Buffer has been destroyed.")

        if sample_type in (SampleType.BYTE, SampleType.UNSIGNED_BYTE):
            bytes_per_sample = 1
        elif sample_type in (SampleType.SHORT, SampleType.UNSIGNED_SHORT):
            bytes_per_sample = 2
        elif sample_type in (SampleType.INT, SampleType.UNSIGNED_INT, SampleType.FLOAT):
            bytes_per_sample = 4
        elif sample_type == SampleType.DOUBLE:
            bytes_per_sample = 8
        else:
            raise TypeError(f"Invalid sample_type provided: {sample_type}")

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
            raise TypeError(f"Invalid channel layout provided: {channels}")

        num_sample_frames = len(samples) // (bytes_per_sample * num_channels)
        
        al.alBufferSamplesSOFT(self._id, samplerate, internal_format, num_sample_frames, channels, sample_type, samples)
                
    @property
    def id(self):
        """The underlying OpenAL buffer ID."""
        return self._id_value

    def _get_int_property(self, param):
        """Internal helper to get an integer property from the buffer."""
        if self._id_value is None:
            raise OalError("Buffer has been destroyed.")
        value = ctypes.c_int()
        al.alGetBufferi(self._id, param, ctypes.byref(value))
        return value.value

    def _get_float_property(self, param):
        """Internal helper to get a float property from the buffer."""
        if self._id_value is None:
            raise OalError("Buffer has been destroyed.")
        value = ctypes.c_float()
        al.alGetBufferf(self._id, param, ctypes.byref(value))
        return value.value

    @property
    def frequency(self):
        """The sample rate of the audio in this buffer, in Hz."""
        return self._get_int_property(al.AL_FREQUENCY)

    @property
    def bits(self):
        """The bit depth (bits per sample) of the audio in this buffer (e.g., 8 or 16)."""
        return self._get_int_property(al.AL_BITS)

    @property
    def channels(self):
        """The number of audio channels in this buffer (1 for mono, 2 for stereo)."""
        return self._get_int_property(al.AL_CHANNELS)

    @property
    def size(self):
        """The size of the audio data in this buffer, in bytes."""
        return self._get_int_property(al.AL_SIZE)

    @property
    def internal_format(self) -> AudioFormat:
        """
        The internal storage format of the buffer.
        Requires the AL_SOFT_buffer_samples extension.
        
        Returns:
            AudioFormat: The format enum corresponding to the internal storage.
        """
        val = self._get_int_property(al.AL_INTERNAL_FORMAT_SOFT)
        return AudioFormat(val)

    @property
    def byte_length(self) -> int:
        """
        The size of the buffer data in bytes.
        Requires the AL_SOFT_buffer_samples extension.
        """
        return self._get_int_property(al.AL_BYTE_LENGTH_SOFT)

    @property
    def sample_length(self) -> int:
        """
        The length of the buffer data in multi-channel sample frames.
        A "sample frame" is a single sample for all channels at one point in time.
        Requires the AL_SOFT_buffer_samples extension.
        """
        return self._get_int_property(al.AL_SAMPLE_LENGTH_SOFT)

    @property
    def sec_length(self) -> float:
        """
        The length of the buffer data in seconds.
        Requires the AL_SOFT_buffer_samples extension.
        """
        return self._get_float_property(al.AL_SEC_LENGTH_SOFT)

    def destroy(self):
        """Releases the OpenAL buffer resource."""
        if self._id_value is not None:
            temp_id = (ctypes.c_uint * 1)(self._id_value)
            al.alDeleteBuffers(1, temp_id)
            self._id_value = None

    def __del__(self):
        if hasattr(self, '_id_value') and self._id_value is not None:
            # We can't reliably call alDeleteBuffers here because the context
            # might already be destroyed. Instead, we warn the user.
            warnings.warn(f"Orphaned Buffer object (ID: {self._id_value}). "
                          "Please explicitly call .destroy() on buffers.",
                          ResourceWarning)
