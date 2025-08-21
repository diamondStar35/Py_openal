"""
PyOpenAL: A Pythonic wrapper for the OpenAL audio library.

This library provides a high-level, object-oriented API for working with
OpenAL, simplifying common tasks such as loading sounds, managing sources
in 3D space, and streaming audio.

Example usage:

    import time
    from pyopenal import open, stream

    # Load a sound entirely into memory
    sound = open("sound.wav")
    sound.play()

    while sound.state == al.AL_PLAYING:
        time.sleep(1)

For more advanced usage, you can manage the device and context directly:

    from pyopenal import Device, Context, al

    with Device() as device:
        with Context(device) as context:
            source = context.create_source("sound.mp3")
            source.play()
"""

from . import al
from . import alc
from . import event_handler
from . import debug
from .enums import PlaybackState, DistanceModel, CaptureFormat
from .helpers import *

from .device import Device, get_default_device, get_available_devices
from .loopback import LoopbackDevice
from .context import Context
from .source import Source
from .source_pool import SourcePool
from .buffer import Buffer
from .exceptions import OalError, OalWarning
from .loaders import open, stream
from .environment import *
from .capture import (
    CaptureDevice,
    get_default_capture_device,
    get_available_capture_devices
)


__all__ = [
    'al',
    'alc',
    'event_handler',
    'Device',
    'LoopbackDevice',
    'Context',
    'Source',
    'SourcePool',
    'Buffer',
    'open',
    'stream',
    'OalError',
    'OalWarning',
    'get_default_device',
    'get_available_devices',
    'PlaybackState',
    'DistanceModel',
    'set_distance_model',
    'get_distance_model',
    'set_doppler_factor',
    'set_speed_of_sound',
    'defer_updates',
    'process_updates',
    'is_buffer_format_supported',
    'get_doppler_factor',
    'get_speed_of_sound',
    'get_available_resamplers',
    'get_default_resampler',
    'CaptureFormat',
    'CaptureDevice',
    'get_default_capture_device',
    'get_available_capture_devices',
    'get_vendor',
    'get_version',
    'get_renderer',
    'get_extensions',
    'seconds_to_nanoseconds',
    'get_future_time',
]
