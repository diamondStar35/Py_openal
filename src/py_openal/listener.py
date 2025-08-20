import ctypes
from . import al

class Listener:
    """Represents the single listener in the OpenAL context."""

    def _set_vector_property(self, param, vec3):
        """Internal helper to set a 3-element vector property."""
        try:
            if len(vec3) != 3:
                raise ValueError("Vector property must have 3 elements (e.g., a tuple or list).")
        except TypeError:
            raise TypeError("Vector property must be a sequence (e.g., a tuple or list).")

        x, y, z = vec3
        if isinstance(x, int):
            al.alListener3i(param, int(x), int(y), int(z))
        else:
            al.alListener3f(param, float(x), float(y), float(z))

    def move(self, delta_vec):
        """
        Moves the listener by a given vector offset.

        Args:
            delta_vec: A 3-element tuple or list (dx, dy, dz).
        """
        current_pos = self.position
        new_pos = (
            current_pos[0] + delta_vec[0],
            current_pos[1] + delta_vec[1],
            current_pos[2] + delta_vec[2]
        )
        self.position = new_pos

    @property
    def gain(self):
        """The master gain for the listener. Default is 1.0."""
        value = ctypes.c_float()
        al.alGetListenerf(al.AL_GAIN, ctypes.byref(value))
        return value.value

    @gain.setter
    def gain(self, value):
        al.alListenerf(al.AL_GAIN, float(value))

    @property
    def position(self):
        """The listener's position in 3D space (x, y, z)."""
        value = (ctypes.c_float * 3)()
        al.alGetListenerfv(al.AL_POSITION, value)
        return tuple(value)

    @position.setter
    def position(self, vec3):
        self._set_vector_property(al.AL_POSITION, vec3)        

    @property
    def velocity(self):
        """The listener's velocity in 3D space (vx, vy, vz)."""
        value = (ctypes.c_float * 3)()
        al.alGetListenerfv(al.AL_VELOCITY, value)
        return tuple(value)

    @velocity.setter
    def velocity(self, vec3):
        self._set_vector_property(al.AL_VELOCITY, vec3)        

    @property
    def orientation(self):
        """
        The listener's orientation as two vectors: 'at' and 'up'.
        The format is (at_x, at_y, at_z, up_x, up_y, up_z).
        """
        value = (ctypes.c_float * 6)()
        al.alGetListenerfv(al.AL_ORIENTATION, value)
        return tuple(value)
        
    @orientation.setter
    def orientation(self, vec6):
        val_array = (ctypes.c_float * 6)(*vec6)
        al.alListenerfv(al.AL_ORIENTATION, val_array)

    @property
    def meters_per_unit(self):
        """
        The scale factor for distance units. Default is 1.0.
        
        This property informs OpenAL about the scale of your coordinate system.
        For example, if your game's world units are in centimeters, you would
        set this to 0.01. This is crucial for realistic distance attenuation
        and EFX reverb calculations.
        """
        value = ctypes.c_float()
        al.alGetListenerf(al.AL_METERS_PER_UNIT, ctypes.byref(value))
        return value.value

    @meters_per_unit.setter
    def meters_per_unit(self, value):
        al.alListenerf(al.AL_METERS_PER_UNIT, float(value))
