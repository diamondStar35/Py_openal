from .. import al
from ..enums import FrequencyShifterDirection
from .effect import Effect

class FrequencyShifter(Effect):
    """
    The Frequency Shifter is a powerful effect that shifts every frequency
    in the input signal by a fixed amount. Unlike a pitch shifter, this
    disrupts the harmonic relationships in the sound, creating metallic,
    dissonant, or robotic textures.
    """
    def _get_effect_type(self):
        return al.AL_EFFECT_FREQUENCY_SHIFTER

    @property
    def frequency(self):
        """
        The amount in Hertz to shift the input signal's frequencies.
        Range [0.0 to 24000.0].
        
        This value is the core of the effect. A positive value will be added to
        all frequencies in the signal, according to the direction parameters.
        Default is 0.0 Hz.
        """
        return self._get_float_property(al.AL_FREQUENCY_SHIFTER_FREQUENCY)

    @frequency.setter
    def frequency(self, value):
        self._set_float_property(al.AL_FREQUENCY_SHIFTER_FREQUENCY, value)

    @property
    def left_direction(self):
        """
        Controls the direction of the frequency shift for the left channel.
        
        Value should be from the pyopenal.FrequencyShifterDirection enum:
        - FrequencyShifterDirection.DOWN (0): Subtracts the `frequency` value.
        - FrequencyShifterDirection.UP (1): Adds the `frequency` value.
        - FrequencyShifterDirection.OFF (2): No shift is applied.
        Default is DOWN.
        """
        return self._get_int_property(al.AL_FREQUENCY_SHIFTER_LEFT_DIRECTION)

    @left_direction.setter
    def left_direction(self, value):
        self._set_int_property(al.AL_FREQUENCY_SHIFTER_LEFT_DIRECTION, value)

    @property
    def right_direction(self):
        """
        Controls the direction of the frequency shift for the right channel.
        
        Value should be from the pyopenal.FrequencyShifterDirection enum:
        - FrequencyShifterDirection.DOWN (0): Subtracts the `frequency` value.
        - FrequencyShifterDirection.UP (1): Adds the `frequency` value.
        - FrequencyShifterDirection.OFF (2): No shift is applied.
        Default is DOWN.
        """
        return self._get_int_property(al.AL_FREQUENCY_SHIFTER_RIGHT_DIRECTION)

    @right_direction.setter
    def right_direction(self, value):
        self._set_int_property(al.AL_FREQUENCY_SHIFTER_RIGHT_DIRECTION, value)
