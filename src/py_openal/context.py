import ctypes
from . import alc
from .exceptions import OalError
from .listener import Listener
from enum import IntEnum
from .enums import EffectType, FilterType

_ATTRIBUTES = {
    'frequency': alc.ALC_FREQUENCY,
    'refresh': alc.ALC_REFRESH,
    'sync': alc.ALC_SYNC,
    'mono_sources': alc.ALC_MONO_SOURCES,
    'stereo_sources': alc.ALC_STEREO_SOURCES,    
    'max_auxiliary_sends': alc.ALC_MAX_AUXILIARY_SENDS,
    
    # HRTF extension attributes
    'hrtf': alc.ALC_HRTF_SOFT,
    'hrtf_id': alc.ALC_HRTF_ID_SOFT,
    
    # Output mode extension attributes
    'format_channels': alc.ALC_FORMAT_CHANNELS_SOFT,
    'format_type': alc.ALC_FORMAT_TYPE_SOFT,
    'output_mode': alc.ALC_OUTPUT_MODE_SOFT,
    'output_limiter': alc.ALC_OUTPUT_LIMITER_SOFT,
}

def _build_attribute_list(attributes_dict):
    """Converts a dictionary of attributes to a C-style integer list."""
    if not attributes_dict:
        return None
    
    attr_list = []
    for key, value in attributes_dict.items():
        key_lower = key.lower()
        if key_lower not in _ATTRIBUTES:
            raise OalError(f"Invalid attribute: '{key}'")
        
        token = _ATTRIBUTES[key_lower]
        
        if isinstance(value, bool):
            attr_list.extend([token, alc.ALC_TRUE if value else alc.ALC_FALSE])
        elif isinstance(value, IntEnum):
            attr_list.extend([token, value.value])
        else:
            attr_list.extend([token, int(value)])
            
    # Add the null terminator
    attr_list.append(0)
    return attr_list

class Context:
    """An OpenAL context for a specific device."""

    def __init__(self, device, **attributes):
        """
        Creates a context on the given device with specified attributes.
        
        Args:
            device: An open PyOpenAL Device object.
            **attributes: Keyword arguments for context creation. Available options:
                - frequency (int): The output sample rate in Hz (e.g., 44100).
                - refresh (int): The refresh rate for mixing, in Hz.
                - sync (bool): If True, the context is synchronous. Default is False.
                - mono_sources (int): The number of mono sources to support.
                - stereo_sources (int): The number of stereo sources to support.
                - hrtf (bool): If True, requests an HRTF-enabled context.
                - hrtf_id (int): A specific HRTF profile ID to use.
                - max_auxiliary_sends (int): The number of auxiliary effect sends.
                - format_channels (OutputMode): The channel configuration for the output.
                - format_type (SampleType): The sample type for the output.
                - output_mode (OutputMode): A specific output mode to request.
                - output_limiter (bool): If True, enables an output limiter.
        """
        if device.is_closed:
            raise OalError("Device must be open to create a context")
        
        attr_list = _build_attribute_list(attributes)
        
        attr_array = None
        if attr_list:
            attr_array = (ctypes.c_int * len(attr_list))(*attr_list)
            
        self._context = alc.alcCreateContext(device._device, attr_array)
        if not self._context:
            raise OalError("Could not create context")

        self._device_obj = device        
        self._as_parameter_ = self._context
        self._listener = Listener()

    @property
    def listener(self):
        """The listener for this context."""
        return self._listener

    @property
    def device(self):
        """The parent Device object this context was created on."""
        return self._device_obj

    def create_source(self, content=None, streaming=False):
        """
        Creates a Source, optionally loading content for it.

        This is a versatile factory method:
        - If content is None: Creates an empty Source.
        - If content is a Buffer: Creates a Source and attaches the buffer.
        - If content is a str (filepath):
            - if streaming=False: Loads the entire file into a new buffer
              and attaches it to the source (like pyopenal.open).
            - if streaming=True: Creates a streaming source for the file
              (like pyopenal.stream).

        Args:
            content (Buffer or str, optional): The audio content for the source.
            streaming (bool, optional): If content is a filepath, this determines
                                        whether to stream the file. Defaults to False.

        Returns:
            Source or SourceStream: A new source object.
        """
        # Imports are placed here to avoid circular dependencies.
        from .source import Source
        from .buffer import Buffer
        from .loaders import open, stream

        if content is None:
            return Source()
        elif isinstance(content, Buffer):
            return Source(content)
        elif isinstance(content, str):
            if streaming:
                return stream(content)
            else:
                # The open() function returns a Source directly
                return open(content)
        else:
            raise TypeError("content must be a Buffer, a filepath string, or None.")

    def create_effect(self, effect_type):
        """
        Creates an EFX effect object of the specified type.

        This acts as a factory for all available effect types.

        Args:
            effect_type (EffectType): The type of effect to create, from the
                                      pyopenal.EffectType enum.

        Returns:
            An instance of the appropriate Effect subclass (e.g., Reverb, Chorus).
        """
        # Imports are placed here to avoid circular dependencies at module load time.
        from .efx.reverb import Reverb
        from .efx.eax_reverb import EAXReverb
        from .efx.chorus import Chorus
        from .efx.distortion import Distortion
        from .efx.echo import Echo
        from .efx.flanger import Flanger
        from .efx.frequency_shifter import FrequencyShifter
        from .efx.vocal_morpher import VocalMorpher
        from .efx.pitch_shifter import PitchShifter
        from .efx.ring_modulator import RingModulator
        from .efx.auto_wah import Autowah
        from .efx.compressor import Compressor
        from .efx.equalizer import Equalizer

        _effect_map = {
            EffectType.REVERB: Reverb,
            EffectType.EAXREVERB: EAXReverb,
            EffectType.CHORUS: Chorus,
            EffectType.DISTORTION: Distortion,
            EffectType.ECHO: Echo,
            EffectType.FLANGER: Flanger,
            EffectType.FREQUENCY_SHIFTER: FrequencyShifter,
            EffectType.VOCAL_MORPHER: VocalMorpher,
            EffectType.PITCH_SHIFTER: PitchShifter,
            EffectType.RING_MODULATOR: RingModulator,
            EffectType.AUTOWAH: Autowah,
            EffectType.COMPRESSOR: Compressor,
            EffectType.EQUALIZER: Equalizer,
        }

        effect_class = _effect_map.get(effect_type)
        if effect_class:
            return effect_class()
        elif effect_type == EffectType.NULL:
            # The NULL effect doesn't have a class, so we can't instantiate it.
            # It's used to clear slots, not to be created.
            raise ValueError("Cannot create an effect of type NULL.")
        else:
            raise ValueError(f"Unknown or unsupported effect type: {effect_type}")

    def create_effect_slot(self, effect=None):
        """
        Creates an EFX Auxiliary Effect Slot.

        Args:
            effect (Effect, optional): An effect object to load into this slot
                                       upon creation. Defaults to None.

        Returns:
            EffectSlot: A new EffectSlot instance.
        """
        from .efx.slot import EffectSlot
        return EffectSlot(effect)

    def create_filter(self, filter_type):
        """
        Creates an EFX filter object of the specified type.

        Args:
            filter_type (FilterType): The type of filter to create, from the
                                      pyopenal.FilterType enum.

        Returns:
            An instance of the appropriate Filter subclass (e.g., LowPassFilter).
        """
        from .efx.filters import LowPassFilter, HighPassFilter, BandPassFilter

        _filter_map = {
            FilterType.LOWPASS: LowPassFilter,
            FilterType.HIGHPASS: HighPassFilter,
            FilterType.BANDPASS: BandPassFilter,
        }

        filter_class = _filter_map.get(filter_type)
        if filter_class:
            return filter_class()
        elif filter_type == FilterType.NULL:
            raise ValueError("Cannot create a filter of type NULL.")
        else:
            raise ValueError(f"Unknown or unsupported filter type: {filter_type}")
        
    def __enter__(self):
        self.make_current()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.destroy()

    def make_current(self):
        """Makes this context the active one for the current thread."""
        if not alc.alcMakeContextCurrent(self._context):
            raise OalError("Failed to make context current")

    def suspend(self):
        """
        Suspends processing for this context.
        
        All sources playing on this context will stop being processed and
        effectively pause until process() is called.
        """
        if self._context:
            alc.alcSuspendContext(self._context)

    def process(self):
        """
        Resumes processing for a suspended context.
        
        This should be called after suspend() to restart audio processing.
        """
        if self._context:
            alc.alcProcessContext(self._context)

    def destroy(self):
        """Destroys the context and clears the current context for this thread."""
        if self._context:
            alc.alcDestroyContext(self._context)
            alc.alcMakeContextCurrent(None)
            self._context = None
