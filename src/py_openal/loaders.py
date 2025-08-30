import os
import wave
from .buffer import Buffer
from .source import Source
from .stream import SourceStream, _channels_to_al_format
from .exceptions import OalError
from ._internal import _ensure_context

try:
    import miniaudio
    MINIAUDIO_OK = True
except ImportError:
    MINIAUDIO_OK = False

try:
    from pyogg import VorbisFile, VorbisFileStream, OpusFile, OpusFileStream
    PYOGG_OK = True
except ImportError:
    PYOGG_OK = False
    class VorbisFile: pass
    class VorbisFileStream: pass
    class OpusFile: pass
    class OpusFileStream: pass


class WaveFile:
    """Loads a full wave file into memory."""
    def __init__(self, filepath):
        with wave.open(filepath, 'rb') as wf:
            self.channels = wf.getnchannels()
            self.bit_depth = wf.getsampwidth() * 8
            self.frequency = wf.getframerate()
            self.data = wf.readframes(wf.getnframes())
            self.al_format = _channels_to_al_format(self.channels, self.bit_depth)

class WaveFileStream:
    """Provides a streaming interface for a wave file."""
    def __init__(self, filepath):
        self.wf = wave.open(filepath, 'rb')
        self.channels = self.wf.getnchannels()
        self.bit_depth = self.wf.getsampwidth() * 8
        self.frequency = self.wf.getframerate()
        self.is_closed = False

    def get_buffer(self, size):
        """Reads a chunk of data from the file."""
        if self.is_closed:
            return None
        data = self.wf.readframes(size // (self.channels * self.bit_depth // 8))
        if not data:
            self.close()
        return data

    def close(self):
        if not self.is_closed:
            self.wf.close()
            self.is_closed = True

class MiniAudioFile:
    """Loads a full audio file into memory using miniaudio."""
    def __init__(self, filepath):
        decoded = miniaudio.decode_file(filepath)
        self.channels = decoded.nchannels
        self.bit_depth = 16  # miniaudio decodes to 16-bit PCM
        self.frequency = decoded.sample_rate
        self.data = decoded.samples.tobytes()
        self.al_format = _channels_to_al_format(self.channels, self.bit_depth)

class MiniAudioStream:
    """Provides a streaming interface for an audio file using miniaudio."""
    def __init__(self, filepath):
                # miniaudio's stream_file returns a generator
        self._stream_generator = miniaudio.stream_file(filepath)
        
        # We need to pull the first chunk to get the stream info
        first_chunk = next(self._stream_generator)
        self.channels = first_chunk.nchannels
        self.bit_depth = 16 # miniaudio decodes to 16-bit PCM
        self.frequency = first_chunk.sample_rate
        self.is_closed = False        
        self._first_chunk_data = first_chunk.samples.tobytes()

    def get_buffer(self, size):
        """Reads a chunk of data from the file stream."""
        if self.is_closed:
            return None

        # If we have the first chunk stored, return it
        if self._first_chunk_data:
            data = self._first_chunk_data
            self._first_chunk_data = None
            return data

        try:
            chunk = next(self._stream_generator)
            return chunk.samples.tobytes()
        except StopIteration:
            self.close()
            return None

    def close(self):
        if not self.is_closed:
            self.is_closed = True


def open(filepath, extension=None):
    """
    Opens an audio file, loads it into a buffer, and returns a Source.

    Args:
        filepath (str): Path to the audio file.
        extension (str, optional): File extension hint (e.g., '.wav', '.ogg').
                                   Defaults to detecting from filepath.

    Returns:
        A pyopenal.Source object ready for playback.
    """
    _ensure_context()
    if extension is None:
        extension = os.path.splitext(filepath)[1].lower()

    if extension == '.wav':
        audio_file = WaveFile(filepath)
        buf = Buffer(audio_file.al_format, audio_file.data, len(audio_file.data), audio_file.frequency)
        return Source(buf)
    elif PYOGG_OK and extension in ('.ogg', '.opus'):
        ogg_file = VorbisFile(filepath) if extension == '.ogg' else OpusFile(filepath)
        al_format = _channels_to_al_format(ogg_file.channels, 16)
        buf = Buffer(al_format, ogg_file.buffer, len(ogg_file.buffer), ogg_file.frequency)
        return Source(buf)
    elif MINIAUDIO_OK and extension in ('.mp3', '.flac'):
        audio_file = MiniAudioFile(filepath)
        buf = Buffer(audio_file.al_format, audio_file.data, len(audio_file.data), audio_file.frequency)
        return Source(buf)
    else:
        raise OalError(f"Unsupported file format: {extension}. Or required library (PyOgg) is not installed.")

def stream(filepath, extension=None, buffer_count=3, buffer_size=4096 * 8):
    """
    Opens an audio file for streaming and returns a SourceStream.

    Args:
        filepath (str): Path to the audio file.
        extension (str, optional): File extension hint (e.g., '.wav', '.ogg').
                                   Defaults to detecting from filepath.
        buffer_count (int, optional): The number of internal buffers to use for
                                      streaming. Defaults to 3.
        buffer_size (int, optional): The size of each internal buffer in bytes.
                                     Defaults to 32768.

    Returns:
        A pyopenal.SourceStream object ready for playback.
    """
    _ensure_context()
    if extension is None:
        extension = os.path.splitext(filepath)[1].lower()

    if extension == '.wav':
        audio_stream = WaveFileStream(filepath)
        return SourceStream(audio_stream, buffer_count=buffer_count, buffer_size=buffer_size)
    elif PYOGG_OK and extension in ('.ogg', '.opus'):
        audio_stream = VorbisFileStream(filepath) if extension == '.ogg' else OpusFileStream(filepath)
        return SourceStream(audio_stream, buffer_count=buffer_count, buffer_size=buffer_size)
    elif MINIAUDIO_OK and extension in ('.mp3', '.flac'):
        audio_stream = MiniAudioStream(filepath)
        return SourceStream(audio_stream, buffer_count=buffer_count, buffer_size=buffer_size)
    else:
        raise OalError(f"Unsupported file format for streaming: {extension}. Or required library (PyOgg) is not installed.")
