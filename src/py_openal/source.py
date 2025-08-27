import ctypes
import warnings
import sys
from . import al
from .al import _get_al_ext_proc, ALint64SOFT
from .enums import PlaybackState, SourceType, DirectChannelsRemixMode, SpatializeMode, StereoMode
from .environment import get_available_resamplers

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
        self._direct_filter_cache = None
                
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

    def play_at_time(self, device_clock_time: int):
        """
        Schedules the source to start playing at a specific device clock time.
        Requires the AL_SOFT_source_start_delay extension.

        Args:
            device_clock_time (int): The absolute time in nanoseconds on the
                                     device's clock when playback should begin.
                                     Use device.get_clock() and helpers.get_future_time()
                                     to calculate this value.
        """
        
        proc = _get_al_ext_proc(
            'alSourcePlayAtTimeSOFT',
            [ctypes.c_uint, ALint64SOFT],
            None
        )
        proc(self._id, device_clock_time)

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
        """The current playback state (e.g., PlaybackState.PLAYING)."""
        value = ctypes.c_int()
        al.alGetSourcei(self._id, al.AL_SOURCE_STATE, ctypes.byref(value))
        return PlaybackState(value.value)

    @property
    def source_type(self) -> SourceType:
        """
        The type of the source. Read-only.

        Returns:
            SourceType: The source type enumeration, which can be one of:
                 - SourceType.STATIC: A single buffer is attached.
                 - SourceType.STREAMING: Buffers are queued for streaming.
                 - SourceType.UNDETERMINED: No buffer is attached.
        """
        value = self._get_int_property(al.AL_SOURCE_TYPE)
        return SourceType(value)

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
    def sample_offset_clock(self) -> int:
        """
        The playback position in samples, relative to the device clock.
        This is a high-precision 64-bit integer value.
        Requires the AL_SOFT_source_latency extension.
        """
        return self._get_int64_property(al.AL_SAMPLE_OFFSET_CLOCK_SOFT)

    @property
    def sec_offset_clock(self) -> int:
        """
        The playback position in nanoseconds, relative to the device clock.
        This is a high-precision 64-bit integer value.
        Requires the AL_SOFT_source_latency extension.
        """
        return self._get_int64_property(al.AL_SEC_OFFSET_CLOCK_SOFT)

    @property
    def sample_offset_with_latency(self) -> int:
        """
        The playback position in samples, plus the device's output latency.
        This provides a more accurate representation of what is currently being heard.
        This is a high-precision 64-bit integer value.
        Requires the AL_SOFT_source_latency extension.
        """
        return self._get_int64_property(al.AL_SAMPLE_OFFSET_LATENCY_SOFT)

    @property
    def sec_offset_with_latency(self) -> float:
        """
        The playback position in seconds, plus the device's output latency.
        This provides a more accurate representation of what is currently being heard.
        This is a high-precision 64-bit double value.
        Requires the AL_SOFT_source_latency extension.
        """
        return self._get_double_property(al.AL_SEC_OFFSET_LATENCY_SOFT)

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

    @property
    def air_absorption_factor(self):
        """
        Controls the amount of high-frequency damping due to air absorption
        over distance. Range [0.0, 10.0]. Default is 0.0.
        
        A higher value means high frequencies are absorbed more quickly.
        """
        return self._get_float_property(al.AL_AIR_ABSORPTION_FACTOR)

    @air_absorption_factor.setter
    def air_absorption_factor(self, value):
        self._set_float_property(al.AL_AIR_ABSORPTION_FACTOR, value)

    @property
    def room_rolloff_factor(self):
        """
        Controls the attenuation of the reverberated (wet) signal over
        distance. Range [0.0, 10.0]. Default is 0.0.
        
        This allows the reverb from a source to fade as the listener moves away.
        """
        return self._get_float_property(al.AL_ROOM_ROLLOFF_FACTOR)

    @room_rolloff_factor.setter
    def room_rolloff_factor(self, value):
        self._set_float_property(al.AL_ROOM_ROLLOFF_FACTOR, value)

    @property
    def cone_outer_gainhf(self):
        """
        Controls the high-frequency gain when the listener is outside the
        source's outer cone. Range [0.0, 1.0]. Default is 1.0.
        
        This allows for muffling the treble of a sound when you are not
        facing it, in addition to reducing its overall gain.
        """
        return self._get_float_property(al.AL_CONE_OUTER_GAINHF)

    @cone_outer_gainhf.setter
    def cone_outer_gainhf(self, value):
        self._set_float_property(al.AL_CONE_OUTER_GAINHF, value)

    @property
    def direct_filter_gainhf_auto(self):
        """
        When True, automatically applies a low-pass filter to the direct
        (dry) signal based on the air_absorption_factor. Boolean.
        Default is True.
        """
        return self._get_int_property(al.AL_DIRECT_FILTER_GAINHF_AUTO) == al.AL_TRUE

    @direct_filter_gainhf_auto.setter
    def direct_filter_gainhf_auto(self, value):
        self._set_int_property(al.AL_DIRECT_FILTER_GAINHF_AUTO, al.AL_TRUE if value else al.AL_FALSE)

    @property
    def auxiliary_send_filter_gain_auto(self):
        """
        When True, automatically controls the gain of the auxiliary (wet)
        sends based on the source's distance attenuation. Boolean.
        Default is True.
        """
        return self._get_int_property(al.AL_AUXILIARY_SEND_FILTER_GAIN_AUTO) == al.AL_TRUE

    @auxiliary_send_filter_gain_auto.setter
    def auxiliary_send_filter_gain_auto(self, value):
        self._set_int_property(al.AL_AUXILIARY_SEND_FILTER_GAIN_AUTO, al.AL_TRUE if value else al.AL_FALSE)

    @property
    def auxiliary_send_filter_gainhf_auto(self):
        """
        When True, automatically applies a low-pass filter to the auxiliary
        (wet) sends based on the air_absorption_factor. Boolean.
        Default is True.
        """
        return self._get_int_property(al.AL_AUXILIARY_SEND_FILTER_GAINHF_AUTO) == al.AL_TRUE

    @auxiliary_send_filter_gainhf_auto.setter
    def auxiliary_send_filter_gainhf_auto(self, value):
        self._set_int_property(al.AL_AUXILIARY_SEND_FILTER_GAINHF_AUTO, al.AL_TRUE if value else al.AL_FALSE)

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
        if isinstance(x, int):
            al.alSource3i(self._id, param, int(x), int(y), int(z))
        else:
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

    def _get_int64_property(self, param):
        value = al.ALint64SOFT()
        al.alGetSourcei64vSOFT(self._id, param, ctypes.byref(value))
        return value.value

    def _get_double_property(self, param):
        value = ctypes.c_double()
        al.alGetSourcedvSOFT(self._id, param, ctypes.byref(value))
        return value.value

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
    def direct_channels(self) -> DirectChannelsRemixMode:
        """
        Controls whether and how the source's channels are mapped directly
        to the output speakers, bypassing the 3D spatializer.

        Can be set to a value from the DirectChannelsRemixMode enum:
        - OFF: (Default) Spatialization is enabled.
        - DROP_UNMATCHED: Direct channels are enabled. Source channels that
          do not map to an output speaker are dropped. (Equivalent to True).
        - REMIX_UNMATCHED: Direct channels are enabled. Unmapped source channels
          are remixed into the available output speakers. Requires the
          AL_SOFT_direct_channels_remix extension.

        Can also be set with a boolean for backward compatibility:
        - True is equivalent to DROP_UNMATCHED.
        - False is equivalent to OFF.
        """
        val = self._get_int_property(al.AL_DIRECT_CHANNELS_SOFT)
        try:
            return DirectChannelsRemixMode(val)
        except ValueError:
            if val == al.AL_TRUE:
                return DirectChannelsRemixMode.DROP_UNMATCHED
            return DirectChannelsRemixMode.OFF

    @direct_channels.setter
    def direct_channels(self, value):
        """
        Sets the direct channels mode for this source.
        """
        if isinstance(value, bool):
            mode = DirectChannelsRemixMode.DROP_UNMATCHED if value else DirectChannelsRemixMode.OFF
            self._set_int_property(al.AL_DIRECT_CHANNELS_SOFT, mode)
        elif isinstance(value, DirectChannelsRemixMode):
            self._set_int_property(al.AL_DIRECT_CHANNELS_SOFT, value)
        else:
            raise TypeError("Value must be a boolean or a DirectChannelsRemixMode enum member.")

    @property
    def direct_filter(self):
        """
        The EFX filter applied to the source's direct (non-reverberated)
        audio path. Set to a Filter object or None.
        
        Note: This is a write-only property in the underlying OpenAL API.
        PyOpenAL caches the last set value to provide a readable property.
        """
        return self._direct_filter_cache

    @direct_filter.setter
    def direct_filter(self, filter_obj):
        """
        Sets the direct path filter. This is the key to controlling the
        dry/wet mix. To mute the dry signal, assign a filter with gain=0.
        
        Args:
            filter_obj (Filter, optional): The filter to apply, or None to clear.
        """
        if self._id_value is None:
            raise OalError("Source has been destroyed.")
            
        filter_id = filter_obj.id if filter_obj is not None else al.AL_FILTER_NULL
        al.alSourcei(self._id, al.AL_DIRECT_FILTER, filter_id)
        self._direct_filter_cache = filter_obj

    @property
    def spatialize(self):
        """
        Controls whether the source's sound is spatialized in 3D space.
        This requires the AL_SOFT_source_spatialize extension.

        Can be set to True, False, or the string 'auto'.
        - True: The source is always spatialized.
        - False: The source is never spatialized (non-directional).
        - 'auto': The implementation decides (typically spatializes mono sources).

        Returns:
            SpatializeMode: The current spatialization mode.
        """
        val = self._get_int_property(al.AL_SOURCE_SPATIALIZE_SOFT)
        return SpatializeMode(val)

    @spatialize.setter
    def spatialize(self, value):
        """
        Sets the spatialization mode for this source.

        Args:
            value (SpatializeMode or bool): The desired mode.
                - SpatializeMode.ON or True: The source is always spatialized.
                - SpatializeMode.OFF or False: The source is never spatialized.
                - SpatializeMode.AUTO: The implementation decides (default).
        """
        if isinstance(value, SpatializeMode):
            self._set_int_property(al.AL_SOURCE_SPATIALIZE_SOFT, value)
        elif isinstance(value, bool):
            mode = SpatializeMode.ON if value else SpatializeMode.OFF
            self._set_int_property(al.AL_SOURCE_SPATIALIZE_SOFT, mode)
        else:
            raise TypeError("Value must be a boolean or a SpatializeMode enum member.")

    @property
    def source_relative(self):
        """Whether the source's position is relative to the listener. Boolean."""
        return self._get_int_property(al.AL_SOURCE_RELATIVE) == al.AL_TRUE

    @source_relative.setter
    def source_relative(self, value):
        self._set_int_property(al.AL_SOURCE_RELATIVE, al.AL_TRUE if value else al.AL_FALSE)

    @property
    def stereo_mode(self) -> StereoMode:
        """
        The stereo playback mode for the source.
        Requires the AL_SOFT_UHJ extension.

        Can be set to a value from the pyopenal.StereoMode enum:
        - StereoMode.NORMAL: Standard stereo playback.
        - StereoMode.SUPER_STEREO: An enhanced stereo mode which can provide
          a wider sound stage. The width is controlled by the
          `super_stereo_width` property.
        """
        val = self._get_int_property(al.AL_STEREO_MODE_SOFT)
        return StereoMode(val)

    @stereo_mode.setter
    def stereo_mode(self, value: StereoMode):
        if not isinstance(value, StereoMode):
            raise TypeError("Value must be a StereoMode enum member.")
        self._set_int_property(al.AL_STEREO_MODE_SOFT, value)

    @property
    def super_stereo_width(self) -> float:
        """
        Controls the width of the 'Super Stereo' effect when `stereo_mode` is
        set to SUPER_STEREO. Range [0.0 to 1.0]. Default is 0.0.
        Requires the AL_SOFT_UHJ extension.
        """
        return self._get_float_property(al.AL_SUPER_STEREO_WIDTH_SOFT)

    @super_stereo_width.setter
    def super_stereo_width(self, value: float):
        self._set_float_property(al.AL_SUPER_STEREO_WIDTH_SOFT, value)

@property
def resampler(self) -> int:
    """
    Gets the index of the resampler being used by this source.
    Requires the AL_SOFT_source_resampler extension.
    
    Use `pyopenal.get_available_resamplers()` to map this index to a name.
    """
    return self._get_int_property(al.AL_SOURCE_RESAMPLER_SOFT)

@resampler.setter
def resampler(self, value):
    """
    Sets the resampler for this source by its name or index.
    Requires the AL_SOFT_source_resampler extension.

    Args:
        value (str or int): The name (e.g., 'sinc4') or index of the
                              resampler to use.
    """
    if isinstance(value, str):        
        resamplers = get_available_resamplers()
        found = False
        for r in resamplers:
            if r['name'] == value:
                self._set_int_property(al.AL_SOURCE_RESAMPLER_SOFT, r['index'])
                found = True
                break
        if not found:
            raise ValueError(f"Resampler name '{value}' not found.")
    elif isinstance(value, int):
        self._set_int_property(al.AL_SOURCE_RESAMPLER_SOFT, value)
    else:
        raise TypeError("Resampler must be set with a string (name) or an integer (index).")
