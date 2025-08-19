import ctypes
import warnings
from . import al

class Buffer:
    def __init__(self, data_format, data, size, frequency):
        """
        Creates an OpenAL buffer and fills it with audio data.
        
        Args:
            data_format: The format of the data (e.g., al.AL_FORMAT_MONO16).
            data: The raw audio data bytes.
            size: The size of the data in bytes.
            frequency: The sample rate of the audio.
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
