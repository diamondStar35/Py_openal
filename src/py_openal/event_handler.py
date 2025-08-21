import ctypes
from collections import namedtuple
from . import al
from . import alc
from .enums import EventType, DeviceEventType, DeviceType

# A user-friendly structure to hold event data
Event = namedtuple('Event', ['type', 'object_id', 'param', 'message'])

# Global variable to hold the user's Python callback function
_user_callback = None

def _c_callback_handler(event_type, obj_id, param, length, message, user_param):
    """
    This is the internal C-level callback function.
    It receives the event from OpenAL and dispatches it to the Python callback.
    """
    if _user_callback:
        try:
            msg_str = message.decode('utf-8') if message else ""            
            # Create a Python-friendly Event object
            event = Event(
                type=EventType(event_type),
                object_id=obj_id,
                param=param,
                message=msg_str
            )
            
            # Call the user's registered Python function
            _user_callback(event)
        except Exception as e:
            print(f"Unhandled exception in OpenAL event callback: {e}")

# Create a C-compatible function pointer from our Python handler
_C_EVENT_CALLBACK = al.ALEVENTPROCSOFT(_c_callback_handler)


def set_event_callback(callback):
    """
    Registers a single callback function to receive OpenAL events.

    The callback function will be invoked from a separate OpenAL thread.
    Ensure that any code within the callback is thread-safe.

    Args:
        callback (callable): A function that accepts a single argument (an
                             `Event` object). The Event object has the
                             following attributes: `type`, `object_id`,
                             `param`, and `message`. Pass `None` to unregister
                             the callback.
    """
    # We must import this here to avoid circular dependencies
    from ._internal import _ensure_context
    _ensure_context()
    global _user_callback
    
    if callback is None:
        # Unregister the callback
        _user_callback = None
        al.alEventCallbackSOFT(al.ALEVENTPROCSOFT(0), None)
    else:
        if not callable(callback):
            raise TypeError("The provided callback must be a callable function or None.")
        
        _user_callback = callback
        al.alEventCallbackSOFT(_C_EVENT_CALLBACK, None)


def control_events(event_types, enable: bool):
    """
    Enables or disables notifications for a list of event types.

    By default, all events are disabled. You must call this to specify which
    events you are interested in receiving.

    Args:
        event_types (list[EventType]): A list of EventType enums to enable
                                       or disable.
        enable (bool): Set to True to enable notifications for these types,
                       False to disable them.
    """
    # We must import this here to avoid circular dependencies
    from ._internal import _ensure_context
    _ensure_context()
    if not event_types:
        return
        
    num_types = len(event_types)
    type_array = (ctypes.c_int * num_types)(*[e.value for e in event_types])
    
    al.alEventControlSOFT(num_types, type_array, al.AL_TRUE if enable else al.AL_FALSE)

# ALC System Event Handling
SystemEvent = namedtuple('SystemEvent', ['type', 'device_type', 'device_name'])
_user_system_callback = None
_alcEventControlSOFT = None
_alcEventCallbackSOFT = None

def _c_system_callback_handler(event_type, device_type, device, length, message, user_param):
    """
    Internal C-level callback for system events.
    Receives events from OpenAL and dispatches them to the Python callback.
    """
    if _user_system_callback:
        try:
            # For system events, the 'message' contains the device name.
            device_name_str = message.decode('utf-8') if message else ""
            
            event = SystemEvent(
                type=DeviceEventType(event_type),
                device_type=DeviceType(device_type),
                device_name=device_name_str
            )
            _user_system_callback(event)
        except Exception as e:
            print(f"Unhandled exception in OpenAL system event callback: {e}")

_C_SYSTEM_EVENT_CALLBACK = alc.ALCEVENTPROCSOFT(_c_system_callback_handler)


def set_system_event_callback(callback):
    """
    Registers a callback for system-level device events.

    The callback will be invoked when devices are added/removed or the
    default device changes.

    Args:
        callback (callable): A function that accepts a single `SystemEvent`
                             argument. Pass `None` to unregister.
    """

    global _alcEventCallbackSOFT, _user_system_callback
    if _alcEventCallbackSOFT is None:
        _alcEventCallbackSOFT = alc._get_alc_ext_proc(
            'alcEventCallbackSOFT',
            [alc.ALCEVENTPROCSOFT, ctypes.c_void_p],
            None
        )
    if not _alcEventCallbackSOFT:
        raise OalError("System event callback is not supported by this OpenAL implementation.")

    if callback is None:
        _user_system_callback = None
        _alcEventCallbackSOFT(alc.ALCEVENTPROCSOFT(0), None)
    else:
        if not callable(callback):
            raise TypeError("The provided callback must be a callable function or None.")
        _user_system_callback = callback
        _alcEventCallbackSOFT(_C_SYSTEM_EVENT_CALLBACK, None)


def control_system_events(event_types, enable: bool):
    """
    Enables or disables notifications for a list of system event types.

    By default, all events are disabled. You must call this to specify which
    events you are interested in receiving.

    Args:
        event_types (list[DeviceEventType]): A list of events to control.
        enable (bool): True to enable, False to disable.
    """

    global _alcEventControlSOFT
    if _alcEventControlSOFT is None:
        _alcEventControlSOFT = alc._get_alc_ext_proc(
            'alcEventControlSOFT',
            [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_uint8],
            None
        )
    if not _alcEventControlSOFT:
        raise OalError("System event control is not supported by this OpenAL implementation.")

    if not event_types:
        return
    num_types = len(event_types)
    type_array = (ctypes.c_int * num_types)(*[e.value for e in event_types])
    _alcEventControlSOFT(num_types, type_array, al.AL_TRUE if enable else al.AL_FALSE)

