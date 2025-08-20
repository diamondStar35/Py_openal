import ctypes
from . import al
from ._internal import _ensure_context
from .exceptions import OalError
from .al import _get_al_ext_proc

def set_distance_model(model):
    """
    Sets the global distance attenuation model for the current context.

    Args:
        model: A value from the pyopenal.DistanceModel enum.
    """
    _ensure_context()
    al.alDistanceModel(model)

def get_distance_model():
    """
    Gets the global distance attenuation model for the current context.

    Returns:
        int: The current distance model value (matches pyopenal.DistanceModel).
    """
    _ensure_context()
    return al.alGetInteger(al.AL_DISTANCE_MODEL)

def set_doppler_factor(factor):
    """
    Sets the global Doppler effect factor.

    A value of 1.0 is normal, 0.0 disables the effect.
    Higher values exaggerate the effect.

    Args:
        factor (float): The Doppler factor.
    """
    _ensure_context()
    al.alDopplerFactor(float(factor))

def set_speed_of_sound(speed):
    """
    Sets the speed of sound for Doppler effect calculations.

    The default is 343.3. Units should be consistent with
    source/listener velocity units (e.g., meters/sec).

    Args:
        speed (float): The speed of sound.
    """
    _ensure_context()
    al.alSpeedOfSound(float(speed))

def defer_updates():
    """
    Begins a block of deferred updates.
    
    After calling this, any changes to OpenAL state (like source positions,
    gains, etc.) will be queued up but not applied until process_updates()
    is called. This is a performance optimization for updating many
    objects at once.
    """
    _ensure_context()
    al.alDeferUpdatesSOFT()

def process_updates():
    """
    Applies all queued changes made since defer_updates() was called.
    """
    _ensure_context()
    al.alProcessUpdatesSOFT()

def is_buffer_format_supported(format_enum):
    """
    Checks if a specific buffer format is supported by the implementation.

    Args:
        format_enum (int): The format to check (e.g., al.AL_FORMAT_STEREO_FLOAT32).

    Returns:
        bool: True if the format is supported, False otherwise.
    """
    _ensure_context()
    return bool(al.alIsBufferFormatSupportedSOFT(format_enum))

def get_doppler_factor():
    """
    Gets the global Doppler effect factor.

    Returns:
        float: The current Doppler factor.
    """
    _ensure_context()
    return al.alGetFloat(al.AL_DOPPLER_FACTOR)

def get_speed_of_sound():
    """
    Gets the speed of sound used for Doppler effect calculations.

    Returns:
        float: The current speed of sound.
    """
    _ensure_context()
    return al.alGetFloat(al.AL_SPEED_OF_SOUND)

def get_vendor():
    """Returns the name of the OpenAL vendor (e.g., 'OpenAL Community')."""
    _ensure_context()
    ptr = al.alGetString(al.AL_VENDOR)
    return ctypes.string_at(ptr).decode('utf-8') if ptr else ""

def get_version():
    """Returns the version string of this OpenAL implementation."""
    _ensure_context()
    ptr = al.alGetString(al.AL_VERSION)
    return ctypes.string_at(ptr).decode('utf-8') if ptr else ""

def get_renderer():
    """Returns the name of the audio renderer (e.g., 'OpenAL Soft')."""
    _ensure_context()
    ptr = al.alGetString(al.AL_RENDERER)
    return ctypes.string_at(ptr).decode('utf-8') if ptr else ""

def get_extensions():
    """
    Returns a list of supported OpenAL extensions.
    
    This is useful for checking if features like EFX effects are available.
    """
    _ensure_context()
    ptr = al.alGetString(al.AL_EXTENSIONS)
    if not ptr:
        return []
    # The result is a single space-separated string
    extensions_str = ctypes.string_at(ptr).decode('utf-8')
    return extensions_str.split(' ')

def get_available_resamplers() -> list[str]:
    """
    Gets a list of the names of available source resamplers.
    Requires the AL_SOFT_source_resampler extension.

    Returns:
        list[str]: A list of resampler names.
    """
    _ensure_context()
    num_resamplers = al.alGetInteger(al.AL_NUM_RESAMPLERS_SOFT)
    
    proc = _get_al_ext_proc('alGetStringiSOFT', [ctypes.c_int, ctypes.c_int], ctypes.c_char_p)
    resamplers = []
    for i in range(num_resamplers):
        name_ptr = proc(al.AL_RESAMPLER_NAME_SOFT, i)
        if name_ptr:
            resamplers.append(name_ptr.decode('utf-8'))
    return resamplers

def get_available_resamplers() -> list[dict]:
    """
    Gets a list of the available source resamplers.
    Requires the AL_SOFT_source_resampler extension.

    Returns:
        list[dict]: A list of dictionaries, where each dictionary has
                    'name' (str) and 'index' (int) keys.
    """
    _ensure_context()
    num_resamplers = al.alGetInteger(al.AL_NUM_RESAMPLERS_SOFT)
    
    from .al import _get_al_ext_proc
    proc = _get_al_ext_proc('alGetStringiSOFT', [ctypes.c_int, ctypes.c_int], ctypes.c_char_p)

    resamplers = []
    for i in range(num_resamplers):
        name_ptr = proc(al.AL_RESAMPLER_NAME_SOFT, i)
        if name_ptr:
            resamplers.append({'name': name_ptr.decode('utf-8'), 'index': i})
    return resamplers

def get_default_resampler() -> str:
    """
    Gets the name of the default source resampler.
    Requires the AL_SOFT_source_resampler extension.

    Returns:
        str: The name of the default resampler.
    """
    _ensure_context()
    resampler_index = al.alGetInteger(al.AL_DEFAULT_RESAMPLER_SOFT)

    from .al import _get_al_ext_proc
    proc = _get_al_ext_proc('alGetStringiSOFT', [ctypes.c_int, ctypes.c_int], ctypes.c_char_p)
    
    name_ptr = proc(al.AL_RESAMPLER_NAME_SOFT, resampler_index)
    if name_ptr:
        return name_ptr.decode('utf-8')
    return ""

