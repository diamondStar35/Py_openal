from .effect import Effect
from .. import al
from .reverb_presets import PRESETS

class Reverb(Effect):
    """
    A Reverb effect, which simulates the acoustic environment of a room.
    """
    def _get_effect_type(self):
        return al.AL_EFFECT_REVERB

    def apply_preset(self, preset_name: str):
        """
        Applies a set of predefined values to this Reverb instance.

        Args:
            preset_name (str): The name of the preset to apply, e.g., 'Room'.
                               Must be a key in the reverb_presets.PRESETS dictionary.
        """
        if preset_name not in PRESETS:
            raise ValueError(f"Preset '{preset_name}' not found for standard Reverb.")
        
        settings = PRESETS[preset_name]
        for key, value in settings.items():
            setattr(self, key, value)

    @property
    def density(self):
        """Controls the coloration of the late reverb. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_REVERB_DENSITY)
    
    @density.setter
    def density(self, value):
        self._set_float_property(al.AL_REVERB_DENSITY, value)

    @property
    def diffusion(self):
        """Controls the echo density in the late reverb decay. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_REVERB_DIFFUSION)
    
    @diffusion.setter
    def diffusion(self, value):
        self._set_float_property(al.AL_REVERB_DIFFUSION, value)

    @property
    def gain(self):
        """The master volume of the reverb effect. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_REVERB_GAIN)
    
    @gain.setter
    def gain(self, value):
        self._set_float_property(al.AL_REVERB_GAIN, value)

    @property
    def gainhf(self):
        """High-frequency gain. Controls the reverb's tonal color. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_REVERB_GAINHF)
    
    @gainhf.setter
    def gainhf(self, value):
        self._set_float_property(al.AL_REVERB_GAINHF, value)

    @property
    def decay_time(self):
        """Reverberation decay time at low frequencies, in seconds. Range [0.1, 20.0]."""
        return self._get_float_property(al.AL_REVERB_DECAY_TIME)
    
    @decay_time.setter
    def decay_time(self, value):
        self._set_float_property(al.AL_REVERB_DECAY_TIME, value)

    @property
    def decay_hfratio(self):
        """Ratio of high-frequency decay time to low-frequency decay time. Range [0.1, 2.0]."""
        return self._get_float_property(al.AL_REVERB_DECAY_HFRATIO)
    
    @decay_hfratio.setter
    def decay_hfratio(self, value):
        self._set_float_property(al.AL_REVERB_DECAY_HFRATIO, value)

    @property
    def reflections_gain(self):
        """Controls the volume of the early reflections. Range [0.0, 3.16]."""
        return self._get_float_property(al.AL_REVERB_REFLECTIONS_GAIN)
    
    @reflections_gain.setter
    def reflections_gain(self, value):
        self._set_float_property(al.AL_REVERB_REFLECTIONS_GAIN, value)

    @property
    def reflections_delay(self):
        """Delay between the direct sound and the first reflection, in seconds. Range [0.0, 0.3]."""
        return self._get_float_property(al.AL_REVERB_REFLECTIONS_DELAY)
    
    @reflections_delay.setter
    def reflections_delay(self, value):
        self._set_float_property(al.AL_REVERB_REFLECTIONS_DELAY, value)

    @property
    def late_reverb_gain(self):
        """Controls the overall volume of the late reverb. Range [0.0, 10.0]."""
        return self._get_float_property(al.AL_REVERB_LATE_REVERB_GAIN)

    @late_reverb_gain.setter
    def late_reverb_gain(self, value):
        self._set_float_property(al.AL_REVERB_LATE_REVERB_GAIN, value)

    @property
    def late_reverb_delay(self):
        """Defines the start time of the late reverb relative to the direct sound. Range [0.0, 0.1]."""
        return self._get_float_property(al.AL_REVERB_LATE_REVERB_DELAY)
    
    @late_reverb_delay.setter
    def late_reverb_delay(self, value):
        self._set_float_property(al.AL_REVERB_LATE_REVERB_DELAY, value)

    @property
    def air_absorption_gainhf(self):
        """Controls the attenuation of high frequencies due to air absorption. Range [0.892, 1.0]."""
        return self._get_float_property(al.AL_REVERB_AIR_ABSORPTION_GAINHF)

    @air_absorption_gainhf.setter
    def air_absorption_gainhf(self, value):
        self._set_float_property(al.AL_REVERB_AIR_ABSORPTION_GAINHF, value)

    @property
    def room_rolloff_factor(self):
        """
        Controls the attenuation of the reverberated (wet) signal over
        distance. Range [0.0, 10.0]. Default is 0.0.
        
        This is a per-effect setting that works in conjunction with the
        per-source `room_rolloff_factor`.
        """
        return self._get_float_property(al.AL_REVERB_ROOM_ROLLOFF_FACTOR)

    @room_rolloff_factor.setter
    def room_rolloff_factor(self, value):
        self._set_float_property(al.AL_REVERB_ROOM_ROLLOFF_FACTOR, value)            

    @property
    def decay_hflimit(self):
        """If true, high-frequency decay is limited by the air absorption gain. Boolean."""
        return self._get_bool_property(al.AL_REVERB_DECAY_HFLIMIT)
        
    @decay_hflimit.setter
    def decay_hflimit(self, value):
        self._set_bool_property(al.AL_REVERB_DECAY_HFLIMIT, value)
