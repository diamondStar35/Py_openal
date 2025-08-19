from .. import al
from .effect import Effect

class Compressor(Effect):
    """
    A compressor that reduces the dynamic range of a sound, making loud parts
    quieter and quiet parts louder. The OpenAL Soft implementation is a simple
    on/off effect with a fixed ratio and threshold.
    """
    def _get_effect_type(self):
        return al.AL_EFFECT_COMPRESSOR

    @property
    def onoff(self):
        """
        Enables or disables the compressor. Boolean. Default is True.
        """
        return self._get_bool_property(al.AL_COMPRESSOR_ONOFF)

    @onoff.setter
    def onoff(self, value):
        self._set_bool_property(al.AL_COMPRESSOR_ONOFF, value)
