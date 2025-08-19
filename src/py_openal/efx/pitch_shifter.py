from .. import al
from .effect import Effect

class PitchShifter(Effect):
    """
    The Pitch Shifter effect changes the pitch of the input signal without
    changing its duration or speed. It preserves the harmonic relationship between
    frequencies, making it ideal for musical pitch adjustments.
    """
    def _get_effect_type(self):
        return al.AL_EFFECT_PITCH_SHIFTER

    @property
    def coarse_tune(self):
        """
        Adjusts the pitch in musical semitones (half-steps).
        Range [-12 to 12].
        
        A value of 12 raises the pitch by one octave. A value of -12 lowers
        it by one octave. Default is 12.
        """
        return self._get_int_property(al.AL_PITCH_SHIFTER_COARSE_TUNE)

    @coarse_tune.setter
    def coarse_tune(self, value):
        self._set_int_property(al.AL_PITCH_SHIFTER_COARSE_TUNE, value)

    @property
    def fine_tune(self):
        """
        Provides fine-grained control over the pitch adjustment in "cents".
        Range [-50 to 50].
        
        A cent is 1/100th of a semitone. This parameter allows for subtle
        detuning effects or precise pitch correction. Default is 0.
        """
        return self._get_int_property(al.AL_PITCH_SHIFTER_FINE_TUNE)

    @fine_tune.setter
    def fine_tune(self, value):
        self._set_int_property(al.AL_PITCH_SHIFTER_FINE_TUNE, value)
