from .. import al
from ..enums import Waveform, Phoneme
from .effect import Effect

class VocalMorpher(Effect):
    """
    An effect that simulates the human vocal tract, allowing you to impose
    vowel-like sounds (phonemes) onto the input signal and morph between them.
    """
    def _get_effect_type(self):
        return al.AL_EFFECT_VOCAL_MORPHER

    @property
    def phonemea(self):
        """
        The first of two phonemes to morph between.
        Value should be from the pyopenal.Phoneme enum. Default is Phoneme.A.
        """
        return self._get_int_property(al.AL_VOCAL_MORPHER_PHONEMEA)

    @phonemea.setter
    def phonemea(self, value):
        self._set_int_property(al.AL_VOCAL_MORPHER_PHONEMEA, value)

    @property
    def phonemeb(self):
        """
        The second of two phonemes to morph between.
        Value should be from the pyopenal.Phoneme enum. Default is Phoneme.ER.
        """
        return self._get_int_property(al.AL_VOCAL_MORPHER_PHONEMEB)

    @phonemeb.setter
    def phonemeb(self, value):
        self._set_int_property(al.AL_VOCAL_MORPHER_PHONEMEB, value)

    @property
    def phonemea_coarse_tuning(self):
        """
        A coarse pitch offset for the first phoneme, in semitones.
        Range [-24 to 24]. Default is 0.
        """
        return self._get_int_property(al.AL_VOCAL_MORPHER_PHONEMEA_COARSE_TUNING)

    @phonemea_coarse_tuning.setter
    def phonemea_coarse_tuning(self, value):
        self._set_int_property(al.AL_VOCAL_MORPHER_PHONEMEA_COARSE_TUNING, value)
    
    @property
    def phonemeb_coarse_tuning(self):
        """
        A coarse pitch offset for the second phoneme, in semitones.
        Range [-24 to 24]. Default is 0.
        """
        return self._get_int_property(al.AL_VOCAL_MORPHER_PHONEMEB_COARSE_TUNING)

    @phonemeb_coarse_tuning.setter
    def phonemeb_coarse_tuning(self, value):
        self._set_int_property(al.AL_VOCAL_MORPHER_PHONEMEB_COARSE_TUNING, value)

    @property
    def waveform(self):
        """
        The LFO shape used to morph between the two phonemes.
        Value should be from the pyopenal.Waveform enum (SINE, TRIANGLE, SAWTOOTH).
        Default is SINE.
        """
        return self._get_int_property(al.AL_VOCAL_MORPHER_WAVEFORM)

    @waveform.setter
    def waveform(self, value):
        self._set_int_property(al.AL_VOCAL_MORPHER_WAVEFORM, value)

    @property
    def rate(self):
        """
        The speed of the LFO morphing between phonemes, in Hz.
        Range [0.0 to 10.0]. Default is 1.41 Hz.
        """
        return self._get_float_property(al.AL_VOCAL_MORPHER_RATE)

    @rate.setter
    def rate(self, value):
        self._set_float_property(al.AL_VOCAL_MORPHER_RATE, value)
