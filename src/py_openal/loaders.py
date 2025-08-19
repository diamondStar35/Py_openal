import os
import wave
from .buffer import Buffer
from .source import Source
from .stream import SourceStream, _channels_to_al_format
from .exceptions import OalError
from ._internal import _ensure_context


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

try:
    from pyogg import VorbisFile, VorbisFileStream, OpusFile, OpusFileStream
    PYOGG_OK = True
except ImportError:
    PYOGG_OK = False
    class VorbisFile: pass
    class VorbisFileStream: pass
    class OpusFile: pass
    class OpusFileStream: pass


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
    else:
        raise OalError(f"Unsupported file format: {extension}. Or required library (PyOgg) is not installed.")


def stream(filepath, extension=None):
    """
    Opens an audio file for streaming and returns a SourceStream.

    Args:
        filepath (str): Path to the audio file.
        extension (str, optional): File extension hint (e.g., '.wav', '.ogg').
                                   Defaults to detecting from filepath.

    Returns:
        A pyopenal.SourceStream object ready for playback.
    """
    _ensure_context()
    if extension is None:
        extension = os.path.splitext(filepath)[1].lower()

    if extension == '.wav':
        audio_stream = WaveFileStream(filepath)
        return SourceStream(audio_stream)
    elif PYOGG_OK and extension in ('.ogg', '.opus'):
        audio_stream = VorbisFileStream(filepath) if extension == '.ogg' else OpusFileStream(filepath)
        return SourceStream(audio_stream)
    else:
        raise OalError(f"Unsupported file format for streaming: {extension}. Or required library (PyOgg) is not installed.")
