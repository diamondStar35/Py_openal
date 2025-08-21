import time
import struct
import random
import math
from collections import namedtuple
from .enums import AudioFormat

# A structure to hold parsed format information
FormatInfo = namedtuple('FormatInfo', ['channels', 'bits', 'bytes_per_sample', 'struct_format'])

# A mapping from our AudioFormat enum to its properties
_format_map = {
    AudioFormat.MONO8:      FormatInfo(1, 8, 1, 'B'),
    AudioFormat.MONO16:     FormatInfo(1, 16, 2, 'h'),
    AudioFormat.MONO_FLOAT32: FormatInfo(1, 32, 4, 'f'),
    AudioFormat.STEREO8:    FormatInfo(2, 8, 1, 'B'),
    AudioFormat.STEREO16:   FormatInfo(2, 16, 2, 'h'),
    AudioFormat.STEREO_FLOAT32: FormatInfo(2, 32, 4, 'f'),
    AudioFormat.QUAD8:      FormatInfo(4, 8, 1, 'B'),
    AudioFormat.QUAD16:     FormatInfo(4, 16, 2, 'h'),
    AudioFormat.QUAD32:     FormatInfo(4, 32, 4, 'f'),
    AudioFormat.SURROUND_5_1_CHN8: FormatInfo(6, 8, 1, 'B'),
    AudioFormat.SURROUND_5_1_CHN16: FormatInfo(6, 16, 2, 'h'),
    AudioFormat.SURROUND_5_1_CHN32: FormatInfo(6, 32, 4, 'f'),
    AudioFormat.SURROUND_6_1_CHN8: FormatInfo(7, 8, 1, 'B'),
    AudioFormat.SURROUND_6_1_CHN16: FormatInfo(7, 16, 2, 'h'),
    AudioFormat.SURROUND_6_1_CHN32: FormatInfo(7, 32, 4, 'f'),
    AudioFormat.SURROUND_7_1_CHN8: FormatInfo(8, 8, 1, 'B'),
    AudioFormat.SURROUND_7_1_CHN16: FormatInfo(8, 16, 2, 'h'),
    AudioFormat.SURROUND_7_1_CHN32: FormatInfo(8, 32, 4, 'f'),
}

def get_format_info(audio_format: AudioFormat) -> FormatInfo:
    """
    Retrieves properties for a given AudioFormat enum.

    Args:
        audio_format (AudioFormat): The format to inspect.

    Returns:
        FormatInfo: A named tuple with channels, bits, bytes_per_sample,
                    and the corresponding `struct` format character.
    """
    try:
        return _format_map[audio_format]
    except KeyError:
        raise ValueError(f"Unsupported or unknown audio format: {audio_format}")


def seconds_to_samples(seconds: float, sample_rate: int) -> int:
    """Converts a duration in seconds to a number of sample frames."""
    return int(seconds * sample_rate)

def samples_to_seconds(samples: int, sample_rate: int) -> float:
    """Converts a number of sample frames to a duration in seconds."""
    return samples / sample_rate

def bytes_to_samples(byte_count: int, audio_format: AudioFormat) -> int:
    """Converts a byte count to a number of sample frames for a given format."""
    info = get_format_info(audio_format)
    bytes_per_frame = info.channels * info.bytes_per_sample
    return byte_count // bytes_per_frame

def samples_to_bytes(samples: int, audio_format: AudioFormat) -> int:
    """Converts a number of sample frames to a byte count for a given format."""
    info = get_format_info(audio_format)
    bytes_per_frame = info.channels * info.bytes_per_sample
    return samples * bytes_per_frame

def seconds_to_bytes(seconds: float, sample_rate: int, audio_format: AudioFormat) -> int:
    """Converts a duration in seconds to a byte count for a given format."""
    samples = seconds_to_samples(seconds, sample_rate)
    return samples_to_bytes(samples, audio_format)

def bytes_to_seconds(byte_count: int, sample_rate: int, audio_format: AudioFormat) -> float:
    """Converts a byte count to a duration in seconds for a given format."""
    samples = bytes_to_samples(byte_count, audio_format)
    return samples_to_seconds(samples, sample_rate)


def _generate_pcm_data(duration, frequency, sample_rate, audio_format, wave_func, amplitude):
    """
    Internal helper to generate and pack periodic waveform data.

    Args:
        duration (float): Duration in seconds.
        frequency (float): Waveform frequency in Hz.
        sample_rate (int): Sample rate in Hz.
        audio_format (AudioFormat): The target audio format.
        wave_func (callable): The function that generates the wave value for a given sample index.
        amplitude (float): The amplitude of the wave [0.0, 1.0].

    Returns:
        bytes: The packed raw audio data for the generated waveform.
    """
    info = get_format_info(audio_format)
    num_sample_frames = seconds_to_samples(duration, sample_rate)
    
    pcm_data = []
    
    # Determine the scaling factor and value range based on the format
    if 'f' in info.struct_format: # Float format
        scale = lambda x: x * amplitude
    elif 'h' in info.struct_format: # 16-bit signed int
        max_val = 32767
        scale = lambda x: int(x * max_val * amplitude)
    elif 'B' in info.struct_format: # 8-bit unsigned int
        max_val = 127.5
        scale = lambda x: int(max_val + (x * max_val * amplitude))
    else:
        raise ValueError("Unsupported format for generation.")

    for i in range(num_sample_frames):
        val = wave_func(i, frequency, sample_rate)
        # Append the same value for each channel (mono compatible)
        for _ in range(info.channels):
            pcm_data.append(scale(val))
            
    return pack_data(pcm_data, audio_format)

def generate_silence(duration: float, sample_rate: int, audio_format: AudioFormat) -> bytes:
    """
    Generates a raw byte string of silent audio data.

    Args:
        duration (float): The duration of the silence in seconds.
        sample_rate (int): The sample rate in Hz.
        audio_format (AudioFormat): The desired audio format.

    Returns:
        bytes: A byte string containing the silent audio data.
    """
    byte_count = seconds_to_bytes(duration, sample_rate, audio_format)
    return b'\x00' * byte_count

def generate_sine_wave(duration: float, frequency: float, sample_rate: int, audio_format: AudioFormat, amplitude: float = 1.0) -> bytes:
    """
    Generates a sine wave.

    Args:
        duration (float): The duration of the wave in seconds.
        frequency (float): The frequency of the wave in Hz.
        sample_rate (int): The sample rate in Hz.
        audio_format (AudioFormat): The desired audio format.
        amplitude (float, optional): The peak amplitude of the wave. Range [0.0, 1.0]. Defaults to 1.0.

    Returns:
        bytes: The packed raw audio data for the generated wave.
    """
    def sine_func(i, freq, sr):
        return math.sin(2 * math.pi * freq * i / sr)
    return _generate_pcm_data(duration, frequency, sample_rate, audio_format, sine_func, amplitude)

def generate_square_wave(duration: float, frequency: float, sample_rate: int, audio_format: AudioFormat, amplitude: float = 1.0) -> bytes:
    """
    Generates a square wave.

    Args:
        duration (float): The duration of the wave in seconds.
        frequency (float): The frequency of the wave in Hz.
        sample_rate (int): The sample rate in Hz.
        audio_format (AudioFormat): The desired audio format.
        amplitude (float, optional): The peak amplitude of the wave. Range [0.0, 1.0]. Defaults to 1.0.

    Returns:
        bytes: The packed raw audio data for the generated wave.
    """
    def square_func(i, freq, sr):
        return 1.0 if math.sin(2 * math.pi * freq * i / sr) >= 0 else -1.0
    return _generate_pcm_data(duration, frequency, sample_rate, audio_format, square_func, amplitude)

def generate_sawtooth_wave(duration: float, frequency: float, sample_rate: int, audio_format: AudioFormat, amplitude: float = 1.0) -> bytes:
    """
    Generates a sawtooth wave.

    Args:
        duration (float): The duration of the wave in seconds.
        frequency (float): The frequency of the wave in Hz.
        sample_rate (int): The sample rate in Hz.
        audio_format (AudioFormat): The desired audio format.
        amplitude (float, optional): The peak amplitude of the wave. Range [0.0, 1.0]. Defaults to 1.0.

    Returns:
        bytes: The packed raw audio data for the generated wave.
    """
    def saw_func(i, freq, sr):
        t = i / sr
        return 2 * (t * freq - math.floor(0.5 + t * freq))
    return _generate_pcm_data(duration, frequency, sample_rate, audio_format, saw_func, amplitude)

def generate_triangle_wave(duration: float, frequency: float, sample_rate: int, audio_format: AudioFormat, amplitude: float = 1.0) -> bytes:
    """
    Generates a triangle wave.

    Args:
        duration (float): The duration of the wave in seconds.
        frequency (float): The frequency of the wave in Hz.
        sample_rate (int): The sample rate in Hz.
        audio_format (AudioFormat): The desired audio format.
        amplitude (float, optional): The peak amplitude of the wave. Range [0.0, 1.0]. Defaults to 1.0.

    Returns:
        bytes: The packed raw audio data for the generated wave.
    """
    def tri_func(i, freq, sr):
        saw = 2 * (i / sr * freq - math.floor(0.5 + i / sr * freq))
        return 2 * abs(saw) - 1
    return _generate_pcm_data(duration, frequency, sample_rate, audio_format, tri_func, amplitude)

def generate_white_noise(duration: float, sample_rate: int, audio_format: AudioFormat, amplitude: float = 1.0) -> bytes:
    """
    Generates white noise.

    Args:
        duration (float): The duration of the noise in seconds.
        sample_rate (int): The sample rate in Hz.
        audio_format (AudioFormat): The desired audio format.
        amplitude (float, optional): The peak amplitude of the noise. Range [0.0, 1.0]. Defaults to 1.0.

    Returns:
        bytes: The packed raw audio data for the generated noise.
    """
    info = get_format_info(audio_format)
    num_samples_total = seconds_to_samples(duration, sample_rate) * info.channels
    
    # Determine the scaling factor and value range based on the format
    if 'f' in info.struct_format: # Float format
        scale = lambda: random.uniform(-1.0, 1.0) * amplitude
    elif 'h' in info.struct_format: # 16-bit signed int
        max_val = int(32767 * amplitude)
        scale = lambda: random.randint(-max_val, max_val)
    elif 'B' in info.struct_format: # 8-bit unsigned int
        max_val = int(127.5 * amplitude)
        scale = lambda: 128 + random.randint(-max_val, max_val)
    else:
        raise ValueError("Unsupported format for generation.")

    pcm_data = [scale() for _ in range(num_samples_total)]
    return pack_data(pcm_data, audio_format)


def pack_data(data: list, audio_format: AudioFormat) -> bytes:
    """
    Packs a list of Python numbers into a raw audio byte string.

    The numbers should be in the appropriate range for the format:
    - 8-bit: Integers from 0 to 255
    - 16-bit: Integers from -32768 to 32767
    - Float32: Floats from -1.0 to 1.0

    Args:
        data (list): A list of numbers representing the audio samples. For
                     multi-channel formats, the data should be interleaved
                     (e.g., [L1, R1, L2, R2, ...]).
        audio_format (AudioFormat): The target audio format.

    Returns:
        bytes: The packed raw audio data.
    """
    info = get_format_info(audio_format)
    format_char = f"<{len(data)}{info.struct_format}"
    return struct.pack(format_char, *data)

def unpack_data(data: bytes, audio_format: AudioFormat) -> list:
    """
    Unpacks a raw audio byte string into a list of Python numbers.

    Args:
        data (bytes): The raw audio data to unpack.
        audio_format (AudioFormat): The format of the source data.

    Returns:
        list: A list of numbers representing the audio samples.
    """
    info = get_format_info(audio_format)
    num_values = len(data) // info.bytes_per_sample
    format_char = f"<{num_values}{info.struct_format}"
    return [val for val_tuple in struct.iter_unpack(format_char, data) for val in val_tuple]

def seconds_to_nanoseconds(seconds: float) -> int:
    """
    Converts a duration in seconds to an integer number of nanoseconds.

    Args:
        seconds (float): The duration in seconds.

    Returns:
        int: The equivalent duration in nanoseconds.
    """
    return int(seconds * 1_000_000_000)

def get_future_time(device_clock: int, delay_in_seconds: float) -> int:
    """
    Calculates a future time on the device's clock.

    This is a convenience function for scheduling sounds to play after a
    certain delay.

    Args:
        device_clock (int): The current device clock time in nanoseconds,
                            typically from `device.get_clock()['clock']`.
        delay_in_seconds (float): The delay from the current clock time
                                  in seconds.

    Returns:
        int: The target absolute clock time in nanoseconds.
    """
    return device_clock + seconds_to_nanoseconds(delay_in_seconds)

