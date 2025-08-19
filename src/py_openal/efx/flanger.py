from .. import al
from ..enums import Waveform
from .effect import Effect

class Flanger(Effect):
    """
    The Flanger effect creates a "swooshing" or "jet engine" sound by mixing
    the audio signal with a slightly delayed and continuously modulated copy
    of itself. It is similar to a Chorus but uses a shorter delay and often
    incorporates feedback.
    """
    def _get_effect_type(self):
        return al.AL_EFFECT_FLANGER

    @property
    def waveform(self):
        """
        The shape of the Low-Frequency Oscillator (LFO) that modulates the delay.
        
        Value should be from the pyopenal.Waveform enum, e.g., Waveform.SINE or
        Waveform.TRIANGLE. Default is TRIANGLE.
        """
        return self._get_int_property(al.AL_FLANGER_WAVEFORM)

    @waveform.setter
    def waveform(self, value):
        self._set_int_property(al.AL_FLANGER_WAVEFORM, value)

    @property
    def phase(self):
        """
        The initial phase of the LFO, in degrees. Range [-180, 180].
        
        Setting different phase shifts for left and right channel flangers can
        create a wider stereo effect. Default is 0.
        """
        return self._get_int_property(al.AL_FLANGER_PHASE)

    @phase.setter
    def phase(self, value):
        self._set_int_property(al.AL_FLANGER_PHASE, value)

    @property
    def rate(self):
        """
        The speed of the LFO, in Hz. Range [0.0 to 10.0].
        
        This determines how quickly the "swoosh" cycles. Default is 0.27 Hz.
        """
        return self._get_float_property(al.AL_FLANGER_RATE)

    @rate.setter
    def rate(self, value):
        self._set_float_property(al.AL_FLANGER_RATE, value)

    @property
    def depth(self):
        """
        The depth of the LFO's modulation. Range [0.0 to 1.0].
        
        This controls the intensity of the flanging effect, essentially how
        wide the "swoosh" is. Default is 1.0.
        """
        return self._get_float_property(al.AL_FLANGER_DEPTH)

    @depth.setter
    def depth(self, value):
        self._set_float_property(al.AL_FLANGER_DEPTH, value)

    @property
    def feedback(self):
        """
        The amount of processed signal fed back into the effect's input.
        Range [-1.0 to 1.0].
        
        Positive feedback creates a more resonant, ringing flange. Negative
        feedback creates a "hollowed-out" sound. Default is -0.5.
        """
        return self._get_float_property(al.AL_FLANGER_FEEDBACK)

    @feedback.setter
    def feedback(self, value):
        self._set_float_property(al.AL_FLANGER_FEEDBACK, value)

    @property
    def delay(self):
        """
        The base delay time for the modulated signal, in seconds.
        Range [0.0 to 0.004].
        
        This very short delay is characteristic of a flanger. Default is 0.002s (2ms).
        """
        return self._get_float_property(al.AL_FLANGER_DELAY)

    @delay.setter
    def delay(self, value):
        self._set_float_property(al.AL_FLANGER_DELAY, value)
