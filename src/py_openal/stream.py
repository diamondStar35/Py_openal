import ctypes
import warnings
from . import al
from .source import Source
from .exceptions import OalWarning

# Default values, can be configured by the user later
STREAM_BUFFER_COUNT = 3  # Use 3 buffers for smoother playback
STREAM_BUFFER_SIZE = 4096 * 8

def _channels_to_al_format(channels, bits):
    """Helper to determine the OpenAL format enum."""
    if channels == 1:
        return al.AL_FORMAT_MONO16 if bits == 16 else al.AL_FORMAT_MONO8
    else:
        return al.AL_FORMAT_STEREO16 if bits == 16 else al.AL_FORMAT_STEREO8

class SourceStream(Source):
    """
    A Source subclass for streaming audio from a file-like object.
    It automatically manages a set of internal buffers.
    """
    def __init__(self, audio_file):
        """
        Creates a streaming source.

        Args:
            audio_file: A file-like object that provides audio data,
                        such as WaveFileStream or a pyogg stream object.
                        It must have `channels`, `frequency`, `bit_depth` (or similar)
                        attributes and a `get_buffer()` method.
        """
        super().__init__()
        self.audio_file = audio_file
        
        # Determine audio format
        # Assuming 16-bit audio if not specified, which is common.
        bits = getattr(audio_file, 'bit_depth', 16) 
        self.al_format = _channels_to_al_format(audio_file.channels, bits)
        
        # Create and manage our own buffers
        self._buffers = (ctypes.c_uint * STREAM_BUFFER_COUNT)()
        al.alGenBuffers(STREAM_BUFFER_COUNT, self._buffers)
        
        self._is_active = True
        self._is_finished = False

        for buf_id in self._buffers:
            self._fill_and_queue_buffer(buf_id)
        
    def _fill_and_queue_buffer(self, buf_id):
        """Fills a single buffer with data from the stream and queues it."""
        if self._is_finished:
            return False
            
        data = self.audio_file.get_buffer(STREAM_BUFFER_SIZE)
        if data:
            al.alBufferData(buf_id, self.al_format, data, len(data), self.audio_file.frequency)
            al.alSourceQueueBuffers(self._id, 1, ctypes.byref(ctypes.c_uint(buf_id)))
            return True
        else:
            # Reached end of stream
            self._is_finished = True
            return False

    def update(self):
        """
        Maintains the stream by refilling and queuing processed buffers.
        This should be called periodically (e.g., once per game loop).
        
        Returns:
            True if the stream is still active, False if it has finished.
        """
        if not self._is_active:
            return False

        processed_count = self._get_int_property(al.AL_BUFFERS_PROCESSED)

        if processed_count > 0:
            processed_buffers = (ctypes.c_uint * processed_count)()
            al.alSourceUnqueueBuffers(self._id, processed_count, processed_buffers)
            
            for buf_id in processed_buffers:
                if not self._fill_and_queue_buffer(buf_id):
                    # No more data to queue, break early
                    break
        
        # If we've run out of buffers to queue and the source has stopped,
        # it means the stream is finished.
        if self._is_finished and self.state != al.AL_PLAYING:
             queued_count = self._get_int_property(al.AL_BUFFERS_QUEUED)
             if queued_count == 0:
                self._is_active = False

        # If the source has stopped playing due to buffer underrun, restart it.
        if self._is_active and not self._is_finished and self.state != al.AL_PLAYING:
            queued_count = self._get_int_property(al.AL_BUFFERS_QUEUED)
            if queued_count > 0:
                warnings.warn(OalWarning("Stream buffer underrun. Consider increasing buffer count or size."))
                self.play()

        return self._is_active

    def destroy(self):
        """Stops the stream and releases all OpenAL resources."""
        if self._id_value is not None:
            self.stop()
            queued_count = self._get_int_property(al.AL_BUFFERS_QUEUED)
            if queued_count > 0:
                processed_buffers = (ctypes.c_uint * queued_count)()
                al.alSourceUnqueueBuffers(self._id, queued_count, processed_buffers)

            al.alDeleteBuffers(STREAM_BUFFER_COUNT, self._buffers)
        
        super().destroy()
