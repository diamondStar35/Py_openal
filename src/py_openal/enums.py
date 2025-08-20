from enum import IntEnum
from . import al
from . import alc

class PlaybackState(IntEnum):
    """Enumeration of possible source playback states."""
    INITIAL = al.AL_INITIAL
    PLAYING = al.AL_PLAYING
    PAUSED = al.AL_PAUSED
    STOPPED = al.AL_STOPPED

    @staticmethod
    def to_string(state_value):
        """Converts a state value to its string representation."""
        if state_value == PlaybackState.INITIAL:
            return "INITIAL"
        if state_value == PlaybackState.PLAYING:
            return "PLAYING"
        if state_value == PlaybackState.PAUSED:
            return "PAUSED"
        if state_value == PlaybackState.STOPPED:
            return "STOPPED"
        return "UNKNOWN"

class DistanceModel(IntEnum):
    """Enumeration of possible distance attenuation models."""
    NONE = al.AL_NONE
    INVERSE_DISTANCE = al.AL_INVERSE_DISTANCE
    INVERSE_DISTANCE_CLAMPED = al.AL_INVERSE_DISTANCE_CLAMPED
    LINEAR_DISTANCE = al.AL_LINEAR_DISTANCE
    LINEAR_DISTANCE_CLAMPED = al.AL_LINEAR_DISTANCE_CLAMPED
    EXPONENT_DISTANCE = al.AL_EXPONENT_DISTANCE
    EXPONENT_DISTANCE_CLAMPED = al.AL_EXPONENT_DISTANCE_CLAMPED

class SourceType(IntEnum):
    """Enumeration of possible source types."""
    STATIC = al.AL_STATIC
    STREAMING = al.AL_STREAMING
    UNDETERMINED = al.AL_UNDETERMINED

class HrtfStatus(IntEnum):
    """
    Enumeration of possible HRTF (Head-Related Transfer Function) states
    on a device. Requires the ALC_SOFT_HRTF extension.
    """
    DISABLED = alc.ALC_HRTF_DISABLED_SOFT
    ENABLED = alc.ALC_HRTF_ENABLED_SOFT
    DENIED = alc.ALC_HRTF_DENIED_SOFT
    REQUIRED = alc.ALC_HRTF_REQUIRED_SOFT
    HEADPHONES_DETECTED = alc.ALC_HRTF_HEADPHONES_DETECTED_SOFT
    UNSUPPORTED_FORMAT = alc.ALC_HRTF_UNSUPPORTED_FORMAT_SOFT

class OutputMode(IntEnum):
    """
    Enumeration of possible device output modes.
    Requires the ALC_SOFT_output_mode extension.
    """
    ANY = alc.ALC_ANY_SOFT
    MONO = alc.ALC_MONO_SOFT
    STEREO = alc.ALC_STEREO_SOFT
    STEREO_BASIC = alc.ALC_STEREO_BASIC_SOFT
    STEREO_UHJ = alc.ALC_STEREO_UHJ_SOFT
    STEREO_HRTF = alc.ALC_STEREO_HRTF_SOFT
    SURROUND_5_1 = alc.ALC_5POINT1_SOFT
    SURROUND_6_1 = alc.ALC_6POINT1_SOFT
    SURROUND_7_1 = alc.ALC_7POINT1_SOFT

class AudioFormat(IntEnum):
    """Enumeration of possible audio buffer formats."""
    # Basic formats
    MONO8 = al.AL_FORMAT_MONO8
    MONO16 = al.AL_FORMAT_MONO16
    STEREO8 = al.AL_FORMAT_STEREO8
    STEREO16 = al.AL_FORMAT_STEREO16

    # Float32 formats
    MONO_FLOAT32 = al.AL_FORMAT_MONO_FLOAT32
    STEREO_FLOAT32 = al.AL_FORMAT_STEREO_FLOAT32

    # Multi-channel formats
    QUAD8 = al.AL_FORMAT_QUAD8
    QUAD16 = al.AL_FORMAT_QUAD16
    QUAD32 = al.AL_FORMAT_QUAD32
    REAR8 = al.AL_FORMAT_REAR8
    REAR16 = al.AL_FORMAT_REAR16
    REAR32 = al.AL_FORMAT_REAR32
    SURROUND_5_1_CHN8 = al.AL_FORMAT_51CHN8
    SURROUND_5_1_CHN16 = al.AL_FORMAT_51CHN16
    SURROUND_5_1_CHN32 = al.AL_FORMAT_51CHN32
    SURROUND_6_1_CHN8 = al.AL_FORMAT_61CHN8
    SURROUND_6_1_CHN16 = al.AL_FORMAT_61CHN16
    SURROUND_6_1_CHN32 = al.AL_FORMAT_61CHN32
    SURROUND_7_1_CHN8 = al.AL_FORMAT_71CHN8
    SURROUND_7_1_CHN16 = al.AL_FORMAT_71CHN16
    SURROUND_7_1_CHN32 = al.AL_FORMAT_71CHN32

    # B-Format (Ambisonic)
    BFORMAT2D_8 = al.AL_FORMAT_BFORMAT2D_8
    BFORMAT2D_16 = al.AL_FORMAT_BFORMAT2D_16
    BFORMAT2D_FLOAT32 = al.AL_FORMAT_BFORMAT2D_FLOAT32
    BFORMAT3D_8 = al.AL_FORMAT_BFORMAT3D_8
    BFORMAT3D_16 = al.AL_FORMAT_BFORMAT3D_16
    BFORMAT3D_FLOAT32 = al.AL_FORMAT_BFORMAT3D_FLOAT32

class CaptureFormat(IntEnum):
    """Enumeration of possible audio capture formats."""
    MONO_8 = al.AL_FORMAT_MONO8
    MONO_16 = al.AL_FORMAT_MONO16
    STEREO_8 = al.AL_FORMAT_STEREO8
    STEREO_16 = al.AL_FORMAT_STEREO16

class EffectType(IntEnum):
    """Enumeration of available EFX effect types."""
    NULL = al.AL_EFFECT_NULL
    REVERB = al.AL_EFFECT_REVERB
    CHORUS = al.AL_EFFECT_CHORUS
    DISTORTION = al.AL_EFFECT_DISTORTION
    ECHO = al.AL_EFFECT_ECHO
    FLANGER = al.AL_EFFECT_FLANGER
    FREQUENCY_SHIFTER = al.AL_EFFECT_FREQUENCY_SHIFTER
    VOCAL_MORPHER = al.AL_EFFECT_VOCAL_MORPHER
    PITCH_SHIFTER = al.AL_EFFECT_PITCH_SHIFTER
    RING_MODULATOR = al.AL_EFFECT_RING_MODULATOR
    AUTOWAH = al.AL_EFFECT_AUTOWAH
    COMPRESSOR = al.AL_EFFECT_COMPRESSOR
    EQUALIZER = al.AL_EFFECT_EQUALIZER
    EAXREVERB = al.AL_EFFECT_EAXREVERB

class FilterType(IntEnum):
    """Enumeration of available EFX filter types."""
    NULL = al.AL_FILTER_NULL
    LOWPASS = al.AL_FILTER_LOWPASS
    HIGHPASS = al.AL_FILTER_HIGHPASS
    BANDPASS = al.AL_FILTER_BANDPASS

class Waveform(IntEnum):
    """
    Enumeration of waveform shapes used by effects like Chorus and Flanger.
    Note that not all effects support all waveforms.
    """
    SINE = 0
    TRIANGLE = 1
    SAWTOOTH = 2
    SQUARE = 2 # Note: Same value as Sawtooth, context is important

class FrequencyShifterDirection(IntEnum):
    """Enumeration for the direction property of the Frequency Shifter effect."""
    DOWN = 0
    UP = 1
    OFF = 2

class Phoneme(IntEnum):
    """Enumeration of phonemes for the Vocal Morpher effect."""
    A = 0; E = 1; I = 2; O = 3; U = 4
    AA = 5; AE = 6; AH = 7; AO = 8; EH = 9
    ER = 10; IH = 11; IY = 12; UH = 13; UW = 14
    B = 15; D = 16; F = 17; G = 18; J = 19
    K = 20; L = 21; M = 22; N = 23; P = 24
    R = 25; S = 26; T = 27; V = 28; Z = 29

class ChannelLayout(IntEnum):
    """
    Enumeration of possible channel layouts for buffer data.
    Used with the AL_SOFT_buffer_samples extension.
    """
    MONO = al.AL_MONO_SOFT
    STEREO = al.AL_STEREO_SOFT
    REAR = al.AL_REAR_SOFT
    QUAD = al.AL_QUAD_SOFT
    SURROUND_5_1 = al.AL_5POINT1_SOFT
    SURROUND_6_1 = al.AL_6POINT1_SOFT
    SURROUND_7_1 = al.AL_7POINT1_SOFT

class SampleType(IntEnum):
    """
    Enumeration of possible sample data types for buffer data.
    Used with the AL_SOFT_buffer_samples extension.
    """
    BYTE = al.AL_BYTE_SOFT
    UNSIGNED_BYTE = al.AL_UNSIGNED_BYTE_SOFT
    SHORT = al.AL_SHORT_SOFT
    UNSIGNED_SHORT = al.AL_UNSIGNED_SHORT_SOFT
    INT = al.AL_INT_SOFT
    UNSIGNED_INT = al.AL_UNSIGNED_INT_SOFT
    FLOAT = al.AL_FLOAT_SOFT
    DOUBLE = al.AL_DOUBLE_SOFT
