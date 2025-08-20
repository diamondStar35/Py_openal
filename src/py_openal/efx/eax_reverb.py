from .effect import Effect
from .. import al
from .eax_presets import PRESETS

class EAXReverb(Effect):
    """
    A more advanced EAX Reverb effect, which simulates the acoustic 
    environment of a room with more detailed parameters.
    """
    def _get_effect_type(self):
        return al.AL_EFFECT_EAXREVERB

    def apply_preset(self, preset_name):
        """
        Applies a set of predefined values to this EAXReverb instance.

        Args:
            preset_name (str): The name of the preset to apply, e.g., 'Concert Hall'.
                               Must be a key in the PRESETS dictionary.
        """
        preset_name = preset_name
        if preset_name not in PRESETS:
            raise ValueError(f"Preset '{preset_name}' not found.")
        
        settings = PRESETS[preset_name]
        for key, value in settings.items():
            setattr(self, key, value)
    
    @property
    def density(self):
        """Controls the coloration of the late reverb. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_EAXREVERB_DENSITY)
    
    @density.setter
    def density(self, value):
        self._set_float_property(al.AL_EAXREVERB_DENSITY, value)

    @property
    def diffusion(self):
        """Controls the echo density in the late reverb decay. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_EAXREVERB_DIFFUSION)
    
    @diffusion.setter
    def diffusion(self, value):
        self._set_float_property(al.AL_EAXREVERB_DIFFUSION, value)

    @property
    def gain(self):
        """The master volume of the reverb effect. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_EAXREVERB_GAIN)
    
    @gain.setter
    def gain(self, value):
        self._set_float_property(al.AL_EAXREVERB_GAIN, value)

    @property
    def gainhf(self):
        """High-frequency gain. Controls the reverb's tonal color. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_EAXREVERB_GAINHF)
    
    @gainhf.setter
    def gainhf(self, value):
        self._set_float_property(al.AL_EAXREVERB_GAINHF, value)

    @property
    def gainlf(self):
        """Low-frequency gain. Controls the reverb's tonal color. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_EAXREVERB_GAINLF)
    
    @gainlf.setter
    def gainlf(self, value):
        self._set_float_property(al.AL_EAXREVERB_GAINLF, value)

    @property
    def decay_time(self):
        """Reverberation decay time, in seconds. Range [0.1, 20.0]."""
        return self._get_float_property(al.AL_EAXREVERB_DECAY_TIME)
    
    @decay_time.setter
    def decay_time(self, value):
        self._set_float_property(al.AL_EAXREVERB_DECAY_TIME, value)

    @property
    def decay_hfratio(self):
        """Ratio of high-frequency decay time to low-frequency decay time. Range [0.1, 2.0]."""
        return self._get_float_property(al.AL_EAXREVERB_DECAY_HFRATIO)
    
    @decay_hfratio.setter
    def decay_hfratio(self, value):
        self._set_float_property(al.AL_EAXREVERB_DECAY_HFRATIO, value)

    @property
    def decay_lfratio(self):
        """Ratio of low-frequency decay time to middle-frequency decay time. Range [0.1, 2.0]."""
        return self._get_float_property(al.AL_EAXREVERB_DECAY_LFRATIO)
    
    @decay_lfratio.setter
    def decay_lfratio(self, value):
        self._set_float_property(al.AL_EAXREVERB_DECAY_LFRATIO, value)

    @property
    def reflections_gain(self):
        """Controls the volume of the early reflections. Range [0.0, 3.16]."""
        return self._get_float_property(al.AL_EAXREVERB_REFLECTIONS_GAIN)
    
    @reflections_gain.setter
    def reflections_gain(self, value):
        self._set_float_property(al.AL_EAXREVERB_REFLECTIONS_GAIN, value)

    @property
    def reflections_delay(self):
        """Delay between the direct sound and the first reflection, in seconds. Range [0.0, 0.3]."""
        return self._get_float_property(al.AL_EAXREVERB_REFLECTIONS_DELAY)
    
    @reflections_delay.setter
    def reflections_delay(self, value):
        self._set_float_property(al.AL_EAXREVERB_REFLECTIONS_DELAY, value)
    
    @property
    def reflections_pan(self):
        """The panning of the early reflections. Expects a 3-element tuple/list (x, y, z)."""
        return self._get_vector_property(al.AL_EAXREVERB_REFLECTIONS_PAN)
        
    @reflections_pan.setter
    def reflections_pan(self, vec3):
        self._set_vector_property(al.AL_EAXREVERB_REFLECTIONS_PAN, vec3)

    @property
    def late_reverb_gain(self):
        """Controls the overall volume of the late reverb. Range [0.0, 10.0]."""
        return self._get_float_property(al.AL_EAXREVERB_LATE_REVERB_GAIN)

    @late_reverb_gain.setter
    def late_reverb_gain(self, value):
        self._set_float_property(al.AL_EAXREVERB_LATE_REVERB_GAIN, value)

    @property
    def late_reverb_delay(self):
        """Defines the start time of the late reverb relative to the direct sound. Range [0.0, 0.1]."""
        return self._get_float_property(al.AL_EAXREVERB_LATE_REVERB_DELAY)
    
    @late_reverb_delay.setter
    def late_reverb_delay(self, value):
        self._set_float_property(al.AL_EAXREVERB_LATE_REVERB_DELAY, value)

    @property
    def late_reverb_pan(self):
        """The panning of the late reverb. Expects a 3-element tuple/list (x, y, z)."""
        return self._get_vector_property(al.AL_EAXREVERB_LATE_REVERB_PAN)
        
    @late_reverb_pan.setter
    def late_reverb_pan(self, vec3):
        self._set_vector_property(al.AL_EAXREVERB_LATE_REVERB_PAN, vec3)

    @property
    def echo_time(self):
        """The delay between echoes. Range [0.075, 0.25]."""
        return self._get_float_property(al.AL_EAXREVERB_ECHO_TIME)

    @echo_time.setter
    def echo_time(self, value):
        self._set_float_property(al.AL_EAXREVERB_ECHO_TIME, value)

    @property
    def echo_depth(self):
        """The amount of feedback in the echo effect. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_EAXREVERB_ECHO_DEPTH)

    @echo_depth.setter
    def echo_depth(self, value):
        self._set_float_property(al.AL_EAXREVERB_ECHO_DEPTH, value)

    @property
    def modulation_time(self):
        """The period of the low-frequency oscillator that modulates the reverb. Range [0.04, 4.0]."""
        return self._get_float_property(al.AL_EAXREVERB_MODULATION_TIME)

    @modulation_time.setter
    def modulation_time(self, value):
        self._set_float_property(al.AL_EAXREVERB_MODULATION_TIME, value)

    @property
    def modulation_depth(self):
        """The amount of modulation to apply. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_EAXREVERB_MODULATION_DEPTH)

    @modulation_depth.setter
    def modulation_depth(self, value):
        self._set_float_property(al.AL_EAXREVERB_MODULATION_DEPTH, value)

    @property
    def air_absorption_gainhf(self):
        """Controls the attenuation of high frequencies due to air absorption. Range [0.892, 1.0]."""
        return self._get_float_property(al.AL_EAXREVERB_AIR_ABSORPTION_GAINHF)

    @air_absorption_gainhf.setter
    def air_absorption_gainhf(self, value):
        self._set_float_property(al.AL_EAXREVERB_AIR_ABSORPTION_GAINHF, value)
    
    @property
    def hfreference(self):
        """The high-frequency reference for air absorption. Range [1000.0, 20000.0]."""
        return self._get_float_property(al.AL_EAXREVERB_HFREFERENCE)
    
    @hfreference.setter
    def hfreference(self, value):
        self._set_float_property(al.AL_EAXREVERB_HFREFERENCE, value)

    @property
    def lfreference(self):
        """The low-frequency reference. Range [20.0, 1000.0]."""
        return self._get_float_property(al.AL_EAXREVERB_LFREFERENCE)

    @lfreference.setter
    def lfreference(self, value):
        self._set_float_property(al.AL_EAXREVERB_LFREFERENCE, value)

    @property
    def room_rolloff_factor(self):
        """Rolloff factor for room reflections. Range [0.0, 10.0]."""
        return self._get_float_property(al.AL_ROOM_ROLLOFF_FACTOR)
    
    @room_rolloff_factor.setter
    def room_rolloff_factor(self, value):
        self._set_float_property(al.AL_ROOM_ROLLOFF_FACTOR, value)
        
    @property
    def decay_hflimit(self):
        """If true, high-frequency decay is limited by the air absorption gain. Boolean."""
        return self._get_bool_property(al.AL_EAXREVERB_DECAY_HFLIMIT)
        
    @decay_hflimit.setter
    def decay_hflimit(self, value):
        self._set_bool_property(al.AL_EAXREVERB_DECAY_HFLIMIT, value)
