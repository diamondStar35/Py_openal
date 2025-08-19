import ctypes
from . import al
from ._internal import _ensure_context

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
