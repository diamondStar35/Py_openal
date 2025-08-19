from . import al

class PlaybackState:
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

class DistanceModel:
    """Enumeration of possible distance attenuation models."""
    NONE = al.AL_NONE
    INVERSE_DISTANCE = al.AL_INVERSE_DISTANCE
    INVERSE_DISTANCE_CLAMPED = al.AL_INVERSE_DISTANCE_CLAMPED
    LINEAR_DISTANCE = al.AL_LINEAR_DISTANCE
    LINEAR_DISTANCE_CLAMPED = al.AL_LINEAR_DISTANCE_CLAMPED
    EXPONENT_DISTANCE = al.AL_EXPONENT_DISTANCE
    EXPONENT_DISTANCE_CLAMPED = al.AL_EXPONENT_DISTANCE_CLAMPED

class CaptureFormat:
    """Enumeration of possible audio capture formats."""
    MONO_8 = al.AL_FORMAT_MONO8
    MONO_16 = al.AL_FORMAT_MONO16
    STEREO_8 = al.AL_FORMAT_STEREO8
    STEREO_16 = al.AL_FORMAT_STEREO16

class EffectType:
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

class FilterType:
    """Enumeration of available EFX filter types."""
    NULL = al.AL_FILTER_NULL
    LOWPASS = al.AL_FILTER_LOWPASS
    HIGHPASS = al.AL_FILTER_HIGHPASS
    BANDPASS = al.AL_FILTER_BANDPASS

class Waveform:
    """
    Enumeration of waveform shapes used by effects like Chorus and Flanger.
    Note that not all effects support all waveforms.
    """
    SINE = 0
    TRIANGLE = 1
    SAWTOOTH = 2
    SQUARE = 2 # Note: Same value as Sawtooth, context is important

class FrequencyShifterDirection:
    """Enumeration for the direction property of the Frequency Shifter effect."""
    DOWN = 0
    UP = 1
    OFF = 2
