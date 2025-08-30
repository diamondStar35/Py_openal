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

class DirectChannelsRemixMode(IntEnum):
    """
    Enumeration of remix modes for direct (non-spatialized) channels.
    """
    OFF = al.AL_FALSE
    DROP_UNMATCHED = al.AL_DROP_UNMATCHED_SOFT
    REMIX_UNMATCHED = al.AL_REMIX_UNMATCHED_SOFT

class SpatializeMode(IntEnum):
    """
    Enumeration of modes for source spatialization.
    """
    OFF = al.AL_FALSE
    ON = al.AL_TRUE
    AUTO = al.AL_AUTO_SOFT

class StereoMode(IntEnum):
    """
    Enumeration of stereo modes for a source.
    Requires the AL_SOFT_UHJ extension.
    """
    NORMAL = al.AL_NORMAL_SOFT
    SUPER_STEREO = al.AL_SUPER_STEREO_SOFT

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

class HrtfMode(IntEnum):
    """
    Enumeration for enabling or disabling HRTF on a device context.
    """
    DISABLED = alc.ALC_FALSE
    ENABLED = alc.ALC_TRUE

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

    # UHJ (Ambisonic)
    UHJ2CHN8 = al.AL_FORMAT_UHJ2CHN8_SOFT
    UHJ2CHN16 = al.AL_FORMAT_UHJ2CHN16_SOFT
    UHJ2CHN_FLOAT32 = al.AL_FORMAT_UHJ2CHN_FLOAT32_SOFT
    UHJ3CHN8 = al.AL_FORMAT_UHJ3CHN8_SOFT
    UHJ3CHN16 = al.AL_FORMAT_UHJ3CHN16_SOFT
    UHJ3CHN_FLOAT32 = al.AL_FORMAT_UHJ3CHN_FLOAT32_SOFT
    UHJ4CHN8 = al.AL_FORMAT_UHJ4CHN8_SOFT
    UHJ4CHN16 = al.AL_FORMAT_UHJ4CHN16_SOFT
    UHJ4CHN_FLOAT32 = al.AL_FORMAT_UHJ4CHN_FLOAT32_SOFT

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

class EventType(IntEnum):
    """
    Enumeration of event types for asynchronous notifications.
    Requires the AL_SOFT_events extension.
    """
    BUFFER_COMPLETED = al.AL_EVENT_TYPE_BUFFER_COMPLETED_SOFT
    SOURCE_STATE_CHANGED = al.AL_EVENT_TYPE_SOURCE_STATE_CHANGED_SOFT
    DISCONNECTED = al.AL_EVENT_TYPE_DISCONNECTED_SOFT

class DeviceEventType(IntEnum):
    """
    Enumeration of system-level device event types for asynchronous notifications.
    Requires the ALC_SOFT_system_events extension.
    """
    DEFAULT_DEVICE_CHANGED = alc.ALC_EVENT_TYPE_DEFAULT_DEVICE_CHANGED_SOFT
    DEVICE_ADDED = alc.ALC_EVENT_TYPE_DEVICE_ADDED_SOFT
    DEVICE_REMOVED = alc.ALC_EVENT_TYPE_DEVICE_REMOVED_SOFT

class DeviceType(IntEnum):
    """
    Enumeration of audio device types.
    Used by the ALC_SOFT_system_events extension.
    """
    PLAYBACK = alc.ALC_PLAYBACK_DEVICE_SOFT
    CAPTURE = alc.ALC_CAPTURE_DEVICE_SOFT

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
    BFORMAT3D = alc.ALC_BFORMAT3D_SOFT

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

class AmbisonicLayout(IntEnum):
    """
    Enumeration of channel layouts for Ambisonic (B-Format) buffer data.
    Requires the AL_SOFT_bformat_ex extension.
    """
    FUMA = al.AL_FUMA_SOFT  # Furse-Malham channel ordering (WXYZ)
    ACN = al.AL_ACN_SOFT   # Ambisonic Channel Number ordering

class AmbisonicScaling(IntEnum):
    """
    Enumeration of normalization scaling for Ambisonic (B-Format) buffer data.
    Requires the AL_SOFT_bformat_ex extension.
    """
    FUMA = al.AL_FUMA_SOFT    # Furse-Malham scaling
    SN3D = al.AL_SN3D_SOFT    # Schmidt Semi-Normalization
    N3D = al.AL_N3D_SOFT      # Full 3D Normalization

class DebugSource(IntEnum):
    """
    Enumeration of possible sources for a debug message.
    Requires the AL_EXT_debug extension.
    """
    API = al.AL_DEBUG_SOURCE_API_EXT
    AUDIO_SYSTEM = al.AL_DEBUG_SOURCE_AUDIO_SYSTEM_EXT
    THIRD_PARTY = al.AL_DEBUG_SOURCE_THIRD_PARTY_EXT
    APPLICATION = al.AL_DEBUG_SOURCE_APPLICATION_EXT
    OTHER = al.AL_DEBUG_SOURCE_OTHER_EXT

class DebugType(IntEnum):
    """
    Enumeration of possible types for a debug message.
    Requires the AL_EXT_debug extension.
    """
    ERROR = al.AL_DEBUG_TYPE_ERROR_EXT
    DEPRECATED_BEHAVIOR = al.AL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_EXT
    UNDEFINED_BEHAVIOR = al.AL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_EXT
    PORTABILITY = al.AL_DEBUG_TYPE_PORTABILITY_EXT
    PERFORMANCE = al.AL_DEBUG_TYPE_PERFORMANCE_EXT
    MARKER = al.AL_DEBUG_TYPE_MARKER_EXT
    PUSH_GROUP = al.AL_DEBUG_TYPE_PUSH_GROUP_EXT
    POP_GROUP = al.AL_DEBUG_TYPE_POP_GROUP_EXT
    OTHER = al.AL_DEBUG_TYPE_OTHER_EXT

class DebugSeverity(IntEnum):
    """
    Enumeration of possible severity levels for a debug message.
    Requires the AL_EXT_debug extension.
    """
    HIGH = al.AL_DEBUG_SEVERITY_HIGH_EXT
    MEDIUM = al.AL_DEBUG_SEVERITY_MEDIUM_EXT
    LOW = al.AL_DEBUG_SEVERITY_LOW_EXT
    NOTIFICATION = al.AL_DEBUG_SEVERITY_NOTIFICATION_EXT

