from .. import al
from ..enums import Waveform
from .effect import Effect

class Chorus(Effect):
    """
    The Chorus effect creates a richer, fuller sound by mixing the original
    signal with slightly delayed and pitch-modulated copies of itself. This
    simulates the sound of multiple voices or instruments playing in unison.
    """
    def _get_effect_type(self):
        return al.AL_EFFECT_CHORUS

    @property
    def waveform(self):
        """
        The shape of the Low-Frequency Oscillator (LFO) used to modulate the pitch.
        
        Value should be from the pyopenal.Waveform enum, e.g., Waveform.SINE or
        Waveform.TRIANGLE. A triangle wave creates a more pronounced and regular
        chorus, while a sine wave is smoother. Default is TRIANGLE.
        """
        return self._get_int_property(al.AL_CHORUS_WAVEFORM)

    @waveform.setter
    def waveform(self, value):
        self._set_int_property(al.AL_CHORUS_WAVEFORM, value)

    @property
    def phase(self):
        """
        The initial phase of the LFO, in degrees. Range [-180, 180].
        
        Setting different phase shifts for two separate chorus effects can create
        a wider stereo imaging effect. Default is 90.
        """
        return self._get_int_property(al.AL_CHORUS_PHASE)

    @phase.setter
    def phase(self, value):
        self._set_int_property(al.AL_CHORUS_PHASE, value)

    @property
    def rate(self):
        """
        The speed of the LFO, in Hz. Range [0.0, 10.0].
        
        This determines how quickly the pitch of the delayed signal fluctuates.
        Higher values create a faster, more shimmering chorus. Default is 1.1 Hz.
        """
        return self._get_float_property(al.AL_CHORUS_RATE)

    @rate.setter
    def rate(self, value):
        self._set_float_property(al.AL_CHORUS_RATE, value)

    @property
    def depth(self):
        """
        The depth of the LFO's modulation. Range [0.0, 1.0].
        
        This controls the intensity of the effect, determining how much the
        pitch varies from the original. Higher values result in a more
        dramatic, detuned sound. Default is 0.1.
        """
        return self._get_float_property(al.AL_CHORUS_DEPTH)

    @depth.setter
    def depth(self, value):
        self._set_float_property(al.AL_CHORUS_DEPTH, value)

    @property
    def feedback(self):
        """
        The amount of processed signal fed back into the effect's input.
        Range [-1.0, 1.0].
        
        Positive values create a reinforcing, resonant effect, while negative
        values create a "hollowed-out" or flanger-like sound due to phase
        cancellation. Default is 0.25.
        """
        return self._get_float_property(al.AL_CHORUS_FEEDBACK)

    @feedback.setter
    def feedback(self, value):
        self._set_float_property(al.AL_CHORUS_FEEDBACK, value)

    @property
    def delay(self):
        """
        The base delay time for the modulated signal, in seconds.
        Range [0.0, 0.016].
        
        This is the average time difference between the dry signal and the
        chorus "voices". Default is 0.016 seconds (16ms).
        """
        return self._get_float_property(al.AL_CHORUS_DELAY)

    @delay.setter
    def delay(self, value):
        self._set_float_property(al.AL_CHORUS_DELAY, value)
