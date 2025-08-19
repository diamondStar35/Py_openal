from .. import al
from .effect import Effect

class Equalizer(Effect):
    """
    A 4-band parametric equalizer to shape the tonal characteristics of a sound
    by boosting or cutting specific frequency ranges.
    """
    def _get_effect_type(self):
        return al.AL_EFFECT_EQUALIZER

    @property
    def low_gain(self):
        """Gain for the low-shelf filter. Range [0.126 to 7.943]. Default is 1.0."""
        return self._get_float_property(al.AL_EQUALIZER_LOW_GAIN)

    @low_gain.setter
    def low_gain(self, value):
        self._set_float_property(al.AL_EQUALIZER_LOW_GAIN, value)

    @property
    def low_cutoff(self):
        """Cutoff frequency for the low-shelf, in Hz. Range [50.0 to 800.0]. Default is 200.0."""
        return self._get_float_property(al.AL_EQUALIZER_LOW_CUTOFF)

    @low_cutoff.setter
    def low_cutoff(self, value):
        self._set_float_property(al.AL_EQUALIZER_LOW_CUTOFF, value)

    @property
    def mid1_gain(self):
        """Gain for the first mid-band. Range [0.126 to 7.943]. Default is 1.0."""
        return self._get_float_property(al.AL_EQUALIZER_MID1_GAIN)

    @mid1_gain.setter
    def mid1_gain(self, value):
        self._set_float_property(al.AL_EQUALIZER_MID1_GAIN, value)

    @property
    def mid1_center(self):
        """Center frequency for the first mid-band, in Hz. Range [200.0 to 3000.0]. Default is 500.0."""
        return self._get_float_property(al.AL_EQUALIZER_MID1_CENTER)

    @mid1_center.setter
    def mid1_center(self, value):
        self._set_float_property(al.AL_EQUALIZER_MID1_CENTER, value)

    @property
    def mid1_width(self):
        """Width (Q factor) of the first mid-band. Range [0.01 to 1.0]. Default is 1.0."""
        return self._get_float_property(al.AL_EQUALIZER_MID1_WIDTH)

    @mid1_width.setter
    def mid1_width(self, value):
        self._set_float_property(al.AL_EQUALIZER_MID1_WIDTH, value)
        
    @property
    def mid2_gain(self):
        """Gain for the second mid-band. Range [0.126 to 7.943]. Default is 1.0."""
        return self._get_float_property(al.AL_EQUALIZER_MID2_GAIN)

    @mid2_gain.setter
    def mid2_gain(self, value):
        self._set_float_property(al.AL_EQUALIZER_MID2_GAIN, value)

    @property
    def mid2_center(self):
        """Center frequency for the second mid-band, in Hz. Range [1000.0 to 8000.0]. Default is 3000.0."""
        return self._get_float_property(al.AL_EQUALIZER_MID2_CENTER)

    @mid2_center.setter
    def mid2_center(self, value):
        self._set_float_property(al.AL_EQUALIZER_MID2_CENTER, value)

    @property
    def mid2_width(self):
        """Width (Q factor) of the second mid-band. Range [0.01 to 1.0]. Default is 1.0."""
        return self._get_float_property(al.AL_EQUALIZER_MID2_WIDTH)

    @mid2_width.setter
    def mid2_width(self, value):
        self._set_float_property(al.AL_EQUALIZER_MID2_WIDTH, value)
        
    @property
    def high_gain(self):
        """Gain for the high-shelf filter. Range [0.126 to 7.943]. Default is 1.0."""
        return self._get_float_property(al.AL_EQUALIZER_HIGH_GAIN)

    @high_gain.setter
    def high_gain(self, value):
        self._set_float_property(al.AL_EQUALIZER_HIGH_GAIN, value)

    @property
    def high_cutoff(self):
        """Cutoff frequency for the high-shelf, in Hz. Range [4000.0 to 16000.0]. Default is 6000.0."""
        return self._get_float_property(al.AL_EQUALIZER_HIGH_CUTOFF)

    @high_cutoff.setter
    def high_cutoff(self, value):
        self._set_float_property(al.AL_EQUALIZER_HIGH_CUTOFF, value)
