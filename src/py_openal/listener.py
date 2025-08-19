import ctypes
from . import al

class Listener:
    """Represents the single listener in the OpenAL context."""

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
        al.alGetListenerf(al.AL_GAIN, value)
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
        x, y, z = vec3
        al.alListener3f(al.AL_POSITION, float(x), float(y), float(z))
        
    @property
    def velocity(self):
        """The listener's velocity in 3D space (vx, vy, vz)."""
        value = (ctypes.c_float * 3)()
        al.alGetListenerfv(al.AL_VELOCITY, value)
        return tuple(value)

    @velocity.setter
    def velocity(self, vec3):
        x, y, z = vec3
        al.alListener3f(al.AL_VELOCITY, float(x), float(y), float(z))
        
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
