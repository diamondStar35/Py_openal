from .. import al
from .effect import Effect

class Distortion(Effect):
    """
    The Distortion effect simulates clipping of an audio signal. Clipping can
    add warmth and harmonic richness, or create aggressive, overdriven sounds.
    """
    def _get_effect_type(self):
        return al.AL_EFFECT_DISTORTION

    @property
    def edge(self):
        """
        Controls the character and harshness of the distortion. Range [0.0, 1.0].
        
        Higher values lead to a brighter, fizzier, and more aggressive sound.
        Lower values produce a smoother, warmer distortion. Default is 0.2.
        """
        return self._get_float_property(al.AL_DISTORTION_EDGE)

    @edge.setter
    def edge(self, value):
        self._set_float_property(al.AL_DISTORTION_EDGE, value)

    @property
    def gain(self):
        """
        The overall gain applied to the signal after distortion. Range [0.01 to 1.0].
        
        Since distortion adds harmonics and can increase the perceived volume,
        this is often used to tame the output level. Default is 0.05.
        """
        return self._get_float_property(al.AL_DISTORTION_GAIN)

    @gain.setter
    def gain(self, value):
        self._set_float_property(al.AL_DISTORTION_GAIN, value)

    @property
    def lowpass_cutoff(self):
        """
        The cutoff frequency for the low-pass filter applied after distortion,
        in Hz. Range [80.0, 24000.0].
        
        This is useful for smoothing out the harsh high-frequency "fizz" that
        distortion can create. Default is 8000.0 Hz.
        """
        return self._get_float_property(al.AL_DISTORTION_LOWPASS_CUTOFF)

    @lowpass_cutoff.setter
    def lowpass_cutoff(self, value):
        self._set_float_property(al.AL_DISTORTION_LOWPASS_CUTOFF, value)

    @property
    def eqcenter(self):
        """
        The center frequency of the post-distortion band-pass filter, in Hz.
        Range [80.0, 24000.0].
        
        This allows you to emphasize a specific tonal range of the distorted
        sound, like boosting the midrange for a "honky" sound. Default is 3600.0 Hz.
        """
        return self._get_float_property(al.AL_DISTORTION_EQCENTER)

    @eqcenter.setter
    def eqcenter(self, value):
        self._set_float_property(al.AL_DISTORTION_EQCENTER, value)

    @property
    def eqbandwidth(self):
        """
        The bandwidth of the post-distortion band-pass filter, in Hz.
        Range [80.0, 24000.0].
        
        This controls how narrow or wide the EQ boost/cut is around the eqcenter
        frequency. Default is 3600.0 Hz.
        """
        return self._get_float_property(al.AL_DISTORTION_EQBANDWIDTH)

    @eqbandwidth.setter
    def eqbandwidth(self, value):
        self._set_float_property(al.AL_DISTORTION_EQBANDWIDTH, value)
