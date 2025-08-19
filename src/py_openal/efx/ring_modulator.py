from .. import al
from ..enums import Waveform
from .effect import Effect

class RingModulator(Effect):
    """
    A ring modulator multiplies the input signal by a carrier wave, creating
    complex sidebands that can sound metallic, bell-like, or robotic.
    """
    def _get_effect_type(self):
        return al.AL_EFFECT_RING_MODULATOR

    @property
    def frequency(self):
        """
        The frequency of the carrier wave, in Hz. Range [0.0 to 8000.0].
        This is the primary control for the timbre of the effect. Default is 440.0 Hz.
        """
        return self._get_float_property(al.AL_RING_MODULATOR_FREQUENCY)

    @frequency.setter
    def frequency(self, value):
        self._set_float_property(al.AL_RING_MODULATOR_FREQUENCY, value)

    @property
    def highpass_cutoff(self):
        """
        The cutoff frequency for a high-pass filter applied after modulation,
        in Hz. Range [0.0 to 24000.0].
        This can be used to clean up low-frequency artifacts. Default is 800.0 Hz.
        """
        return self._get_float_property(al.AL_RING_MODULATOR_HIGHPASS_CUTOFF)

    @highpass_cutoff.setter
    def highpass_cutoff(self, value):
        self._set_float_property(al.AL_RING_MODULATOR_HIGHPASS_CUTOFF, value)
        
    @property
    def waveform(self):
        """
        The shape of the carrier wave.
        Value should be from the pyopenal.Waveform enum (SINE, SAWTOOTH, SQUARE).
        Default is SINE.
        """
        return self._get_int_property(al.AL_RING_MODULATOR_WAVEFORM)

    @waveform.setter
    def waveform(self, value):
        self._set_int_property(al.AL_RING_MODULATOR_WAVEFORM, value)
