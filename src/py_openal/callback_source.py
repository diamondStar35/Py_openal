import ctypes
from . import al
from .source import Source
from .buffer import Buffer
from .enums import AudioFormat
from .exceptions import OalError

class CallbackSource(Source):
    """
    A Source subclass for real-time audio generation or custom streaming.

    This source uses a single, special OpenAL buffer that is filled via a
    user-provided Python callback function whenever OpenAL needs more audio
    data. This is highly efficient for procedural audio or custom decoders.
    """
    def __init__(self, callback, audio_format: AudioFormat, frequency: int):
        """
        Creates a source that gets its audio data from a callback.

        Args:
            callback (callable): A Python function that will be called by
                OpenAL to provide audio data. It must accept two arguments:
                `num_bytes` (int): The number of bytes OpenAL is requesting.
                `user_param` (object): A user-defined object (currently None).
                It must return a bytes-like object (e.g., bytes, bytearray)
                containing exactly `num_bytes` of audio data.
            audio_format (AudioFormat): The format of the audio data that the
                callback will provide.
            frequency (int): The sample rate of the audio data.
        """
        if not callable(callback):
            raise TypeError("The provided callback must be a callable function.")

        super().__init__()
        self._user_callback = callback
        
        # This is the internal handler that conforms to the C function signature.
        # It MUST be stored as an instance variable to prevent it from being
        # garbage collected by Python.
        self._c_callback_handler = al.ALBUFFERCALLBACKTYPESOFT(self._c_callback_entry)
        
        self._callback_buffer = Buffer()
        
        # Register our callback with OpenAL for this buffer.
        # We don't use the user_param from OpenAL's side for now.
        al.alBufferCallbackSOFT(
            self._callback_buffer.id,
            audio_format,
            frequency,
            self._c_callback_handler,
            None  # user_param
        )        
        self.buffer = self._callback_buffer

    def _c_callback_entry(self, user_param_ptr, data_ptr, num_bytes):
        """
        This is the entry point called directly from the C OpenAL library.
        It retrieves the requested data from the user's Python callback and
        copies it into the buffer provided by OpenAL.
        """
        try:
            # Call the user's Python function to get the available audio data.
            # The user function can return less than num_bytes.
            audio_data = self._user_callback(num_bytes, None)

            if not audio_data:
                # No data available, return 0 bytes. OpenAL will handle this
                # by playing silence and calling back again later.
                return 0

            bytes_to_copy = len(audio_data)
            if bytes_to_copy > num_bytes:
                # User provided more than requested, truncate.
                bytes_to_copy = num_bytes            
            ctypes.memmove(data_ptr, audio_data, bytes_to_copy)
            
            # Return the ACTUAL number of bytes we copied.
            return bytes_to_copy
        except Exception as e:
            print(f"Exception in audio callback: {e}")
            return 0

    def destroy(self):
        """
        Stops playback and releases all OpenAL resources, including the
        callback buffer.
        """
        if self._id_value is not None:
            # The main source destroy will handle stopping and detaching.
            super().destroy()

        if self._callback_buffer:
            self._callback_buffer.destroy()
            self._callback_buffer = None
