from .. import al
from .effect import Effect

class Autowah(Effect):
    """
    An envelope-following filter that creates a "wah-wah" effect. The filter's
    center frequency sweeps up and down in response to the input signal's volume.
    """
    def _get_effect_type(self):
        return al.AL_EFFECT_AUTOWAH

    @property
    def attack_time(self):
        """
        Time for the filter to sweep from its minimum to maximum frequency when
        the signal gets louder, in seconds. Range [0.0001 to 1.0]. Default is 0.06.
        """
        return self._get_float_property(al.AL_AUTOWAH_ATTACK_TIME)

    @attack_time.setter
    def attack_time(self, value):
        self._set_float_property(al.AL_AUTOWAH_ATTACK_TIME, value)

    @property
    def release_time(self):
        """
        Time for the filter to sweep from its maximum to minimum frequency when
        the signal gets quieter, in seconds. Range [0.0001 to 1.0]. Default is 0.06.
        """
        return self._get_float_property(al.AL_AUTOWAH_RELEASE_TIME)

    @release_time.setter
    def release_time(self, value):
        self._set_float_property(al.AL_AUTOWAH_RELEASE_TIME, value)

    @property
    def resonance(self):
        """
        The resonance or "Q" of the band-pass filter. Range [2.0 to 1000.0].
        Higher values create a sharper, more pronounced "wah" sound. Default is 1000.0.
        """
        return self._get_float_property(al.AL_AUTOWAH_RESONANCE)

    @resonance.setter
    def resonance(self, value):
        self._set_float_property(al.AL_AUTOWAH_RESONANCE, value)
        
    @property
    def peak_gain(self):
        """
        The gain at the filter's resonant peak. Range [0.00003 to 31621.0].
        This controls the volume boost at the "wah" frequency. Default is 11.22.
        """
        return self._get_float_property(al.AL_AUTOWAH_PEAK_GAIN)
        
    @peak_gain.setter
    def peak_gain(self, value):
        self._set_float_property(al.AL_AUTOWAH_PEAK_GAIN, value)
