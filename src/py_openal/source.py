import ctypes
import warnings
import sys
from . import al

MAX_FLOAT = sys.float_info.max

class Source:
    """Represents an OpenAL audio source."""

    def __init__(self, buffer=None):
        """
        Creates an OpenAL source.
        
        Args:
            buffer: An optional Buffer object to attach to this source.
        """
        self._id = ctypes.c_uint()
        al.alGenSources(1, ctypes.byref(self._id))
        self._id_value = self._id.value
        self._buffer = None
        self._distance_model_cache = 'Default'
                
        if buffer:
            self.buffer = buffer

    def __del__(self):
        if hasattr(self, '_id_value') and self._id_value is not None:
            warnings.warn(f"Orphaned Source object (ID: {self._id_value}). "
                          "Please explicitly call .destroy() on sources.",
                          ResourceWarning)

    def destroy(self):
        """Releases the OpenAL source resource."""
        if self._id_value is not None:
            self.stop()
            self.buffer = None  # Detach buffer
            temp_id = (ctypes.c_uint * 1)(self._id_value)
            al.alDeleteSources(1, temp_id)
            self._id_value = None

    def set_auxiliary_send(self, effect_slot, send_index=0, filter=None):
        """
        Sends a portion of this source's audio to an effect slot.

        To disable a send, pass None for the effect_slot.

        Args:
            effect_slot (EffectSlot, optional): The effect slot to send audio to.
                                                Pass None to clear the send.
            send_index (int, optional): Which auxiliary send to use. Most
                                        hardware supports at least one. Defaults to 0.
            filter (Filter, optional): A filter to apply to the audio before it
                                       enters the effect slot. Defaults to None.
        """
        if self._id_value is None:
            raise OalError("Source has been destroyed.")

        slot_id = effect_slot.id if effect_slot is not None else al.AL_EFFECTSLOT_NULL
        filter_id = filter.id if filter is not None else al.AL_FILTER_NULL        
        al.alSource3i(self._id, al.AL_AUXILIARY_SEND_FILTER, slot_id, send_index, filter_id)

    @property
    def id(self):
        """The underlying OpenAL source ID."""
        return self._id_value


    def play(self):
        """Starts or resumes playback."""
        al.alSourcePlay(self._id)

    def stop(self):
        """Stops playback and resets to the beginning."""
        al.alSourceStop(self._id)

    def pause(self):
        """Pauses playback."""
        al.alSourcePause(self._id)
        
    def rewind(self):
        """Resets playback to the beginning."""
        al.alSourceRewind(self._id)
        
    @property
    def state(self):
        """The current playback state (e.g., al.AL_PLAYING)."""
        value = ctypes.c_int()
        al.alGetSourcei(self._id, al.AL_SOURCE_STATE, ctypes.byref(value))
        return value.value

    @property
    def sec_offset(self):
        """The playback position in seconds."""
        return self._get_float_property(al.AL_SEC_OFFSET)

    @sec_offset.setter
    def sec_offset(self, value):
        """Sets the playback position in seconds."""
        self._set_float_property(al.AL_SEC_OFFSET, value)

    @property
    def sample_offset(self):
        """The playback position in samples."""
        return self._get_int_property(al.AL_SAMPLE_OFFSET)

    @sample_offset.setter
    def sample_offset(self, value):
        """Sets the playback position in samples."""
        self._set_int_property(al.AL_SAMPLE_OFFSET, value)

    @property
    def byte_offset(self):
        """The playback position in bytes."""
        return self._get_int_property(al.AL_BYTE_OFFSET)

    @byte_offset.setter
    def byte_offset(self, value):
        """Sets the playback position in bytes."""
        self._set_int_property(al.AL_BYTE_OFFSET, value)

    @property
    def buffer(self):
        """The openal.Buffer object attached to this source."""
        return self._buffer

    @buffer.setter
    def buffer(self, buf):
        if buf is not None:
            al.alSourcei(self._id, al.AL_BUFFER, buf.id)
        else:
            al.alSourcei(self._id, al.AL_BUFFER, 0) # 0 means no buffer
        self._buffer = buf


    def _get_float_property(self, param):
        value = ctypes.c_float()
        al.alGetSourcef(self._id, param, ctypes.byref(value))
        return value.value

    def _set_float_property(self, param, value):
        al.alSourcef(self._id, param, float(value))

    @property
    def gain(self):
        """The source's gain (volume). Range [0.0, ...]. Default 1.0."""
        return self._get_float_property(al.AL_GAIN)

    @gain.setter
    def gain(self, value):
        self._set_float_property(al.AL_GAIN, value)

    @property
    def pitch(self):
        """The source's pitch multiplier. Range [0.5, 2.0]. Default 1.0."""
        return self._get_float_property(al.AL_PITCH)

    @pitch.setter
    def pitch(self, value):
        self._set_float_property(al.AL_PITCH, value)

    @property
    def max_distance(self):
        """The maximum attenuation distance."""
        return self._get_float_property(al.AL_MAX_DISTANCE)

    @max_distance.setter
    def max_distance(self, value):
        self._set_float_property(al.AL_MAX_DISTANCE, value)

    @property
    def rolloff_factor(self):
        """The rolloff factor for distance attenuation. Default 1.0."""
        return self._get_float_property(al.AL_ROLLOFF_FACTOR)

    @rolloff_factor.setter
    def rolloff_factor(self, value):
        self._set_float_property(al.AL_ROLLOFF_FACTOR, value)

    @property
    def reference_distance(self):
        """The reference distance for attenuation calculations. Default 1.0."""
        return self._get_float_property(al.AL_REFERENCE_DISTANCE)

    @reference_distance.setter
    def reference_distance(self, value):
        self._set_float_property(al.AL_REFERENCE_DISTANCE, value)
        
    @property
    def min_gain(self):
        """The minimum gain for this source. Range [0.0, 1.0]. Default 0.0."""
        return self._get_float_property(al.AL_MIN_GAIN)

    @min_gain.setter
    def min_gain(self, value):
        self._set_float_property(al.AL_MIN_GAIN, value)

    @property
    def max_gain(self):
        """The maximum gain for this source. Range [0.0, 1.0]. Default 1.0."""
        return self._get_float_property(al.AL_MAX_GAIN)

    @max_gain.setter
    def max_gain(self, value):
        self._set_float_property(al.AL_MAX_GAIN, value)

    @property
    def cone_outer_gain(self):
        """Gain outside the outer cone. Range [0.0, 1.0]. Default 0.0."""
        return self._get_float_property(al.AL_CONE_OUTER_GAIN)

    @cone_outer_gain.setter
    def cone_outer_gain(self, value):
        self._set_float_property(al.AL_CONE_OUTER_GAIN, value)

    @property
    def cone_inner_angle(self):
        """The inner angle of the sound cone, in degrees. Range [0, 360]."""
        return self._get_float_property(al.AL_CONE_INNER_ANGLE)

    @cone_inner_angle.setter
    def cone_inner_angle(self, value):
        self._set_float_property(al.AL_CONE_INNER_ANGLE, value)

    @property
    def cone_outer_angle(self):
        """The outer angle of the sound cone, in degrees. Range [0, 360]."""
        return self._get_float_property(al.AL_CONE_OUTER_ANGLE)

    @cone_outer_angle.setter
    def cone_outer_angle(self, value):
        self._set_float_property(al.AL_CONE_OUTER_ANGLE, value)


    def _get_vector_property(self, param):
        value = (ctypes.c_float * 3)()
        al.alGetSourcefv(self._id, param, value)
        return tuple(value)

    def _set_vector_property(self, param, vec3):
        try:
            if len(vec3) != 3:
                raise ValueError("Vector property must have 3 elements (e.g., a tuple or list).")
        except TypeError:
            raise TypeError("Vector property must be a sequence (e.g., a tuple or list).")
            
        x, y, z = vec3
        al.alSource3f(self._id, param, float(x), float(y), float(z))

    @property
    def position(self):
        """The source's position in 3D space. Expects a 3-element tuple/list (x, y, z)."""
        return self._get_vector_property(al.AL_POSITION)

    @position.setter
    def position(self, vec3):
        self._set_vector_property(al.AL_POSITION, vec3)

    @property
    def velocity(self):
        """The source's velocity in 3D space. Expects a 3-element tuple or list (vx, vy, vz)."""
        return self._get_vector_property(al.AL_VELOCITY)

    @velocity.setter
    def velocity(self, vec3):
        self._set_vector_property(al.AL_VELOCITY, vec3)

    @property
    def direction(self):
        """The source's direction vector for directional sound cones. Expects a 3-element tuple or list."""
        return self._get_vector_property(al.AL_DIRECTION)

    @direction.setter
    def direction(self, vec3):
        self._set_vector_property(al.AL_DIRECTION, vec3)


    def _get_int_property(self, param):
        value = ctypes.c_int()
        al.alGetSourcei(self._id, param, ctypes.byref(value))
        return value.value

    def _set_int_property(self, param, value):
        al.alSourcei(self._id, param, int(value))

    @property
    def looping(self):
        """Whether the source should loop playback. Boolean."""
        return bool(self._get_int_property(al.AL_LOOPING))

    @looping.setter
    def looping(self, value):
        self._set_int_property(al.AL_LOOPING, value)

    @property
    def distance_model(self):
        """
        The distance model for this source, overriding the global model.
        
        Set to a value from the pyopenal.DistanceModel enum.
        Set to None or 0 to revert to the global listener-based model.
        Note: This is a write-only property in the underlying OpenAL API.
        PyOpenAL caches the last set value to provide a readable property.
        """
        return self._distance_model_cache

    @distance_model.setter
    def distance_model(self, model):
        value = model if model is not None else 0
        self._set_int_property(al.AL_SOURCE_DISTANCE_MODEL, value)
        self._distance_model_cache = model

    @property
    def loop_points(self):
        """
        Gets the loop points for the source.
        
        Returns:
            tuple[int, int]: A tuple containing the (start_sample, end_sample).
                             Returns (0, -1) if not set.
        """
        values = (ctypes.c_int * 2)()
        al.alGetSourceiv(self._id, al.AL_LOOP_POINTS_SOFT, values)
        return (values[0], values[1])

    @loop_points.setter
    def loop_points(self, points):
        """
        Sets the loop start and end points for the source, in samples.
        
        Args:
            points (tuple[int, int]): A tuple of (start_sample, end_sample).
                                      The end_sample is inclusive. A value of -1
                                      for end_sample means the end of the buffer.
        """
        if not isinstance(points, (list, tuple)) or len(points) != 2:
            raise TypeError("loop_points must be a 2-element tuple or list of (start_sample, end_sample).")
        
        start, end = points
        values = (ctypes.c_int * 2)(int(start), int(end))
        al.alSourceiv(self._id, al.AL_LOOP_POINTS_SOFT, values)

    @property
    def stereo_angles(self):
        """
        Gets the source's stereo angles in radians.
        
        This defines the separation of the left and right channels for a stereo source.
        
        Returns:
            tuple[float, float]: A tuple of (left_angle, right_angle).
        """
        values = (ctypes.c_float * 2)()
        al.alGetSourcefv(self._id, al.AL_STEREO_ANGLES, values)
        return (values[0], values[1])

    @stereo_angles.setter
    def stereo_angles(self, angles):
        """
        Sets the source's stereo angles in radians.
        
        For example, setting to (-math.pi/4, math.pi/4) would create a 90-degree
        sound field in front of the source.
        
        Args:
            angles (tuple[float, float]): A tuple of (left_angle, right_angle).
        """
        if not isinstance(angles, (list, tuple)) or len(angles) != 2:
            raise TypeError("stereo_angles must be a 2-element tuple or list.")
        
        left, right = angles
        values = (ctypes.c_float * 2)(float(left), float(right))
        al.alSourcefv(self._id, al.AL_STEREO_ANGLES, values)

    @property
    def source_radius(self):
        """
        Gets the radius of the source.
        
        When the listener is within this radius, the sound is treated as
        ambient and non-directional, preventing harsh stereo flipping.
        """
        return self._get_float_property(al.AL_SOURCE_RADIUS)

    @source_radius.setter
    def source_radius(self, radius):
        """
        Sets the radius of the source. A value > 0 enables the effect.
        
        Args:
            radius (float): The radius in distance units.
        """
        self._set_float_property(al.AL_SOURCE_RADIUS, radius)

    @property
    def direct_channels(self):
        """
        Gets whether direct channel mapping is enabled for this source.
        
        If True, the source's channels are mapped directly to the output
        speakers, bypassing the 3D spatializer.
        """
        return self._get_int_property(al.AL_DIRECT_CHANNELS_SOFT) == al.AL_TRUE

    @direct_channels.setter
    def direct_channels(self, value):
        """
        Enables or disables direct channel mapping for this source.
        
        Set to True to bypass the 3D spatializer. Ideal for background music.
        """
        self._set_int_property(al.AL_DIRECT_CHANNELS_SOFT, al.AL_TRUE if value else al.AL_FALSE)

    @property
    def source_relative(self):
        """Whether the source's position is relative to the listener. Boolean."""
        return self._get_int_property(al.AL_SOURCE_RELATIVE) == al.AL_TRUE

    @source_relative.setter
    def source_relative(self, value):
        self._set_int_property(al.AL_SOURCE_RELATIVE, al.AL_TRUE if value else al.AL_FALSE)
