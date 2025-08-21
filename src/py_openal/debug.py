import ctypes
from collections import namedtuple
from . import al
from .enums import DebugSource, DebugType, DebugSeverity
from .exceptions import OalError

# A user-friendly structure to hold debug message data
DebugMessage = namedtuple('DebugMessage', ['source', 'type', 'id', 'severity', 'message'])

# Global variable to hold the user's Python callback function
_user_debug_callback = None

def _c_debug_callback_handler(source, msg_type, msg_id, severity, length, message, user_param):
    """
    This is the internal C-level callback function.
    It receives the message from OpenAL and dispatches it to the Python callback.
    """
    if _user_debug_callback:
        try:
            msg_str = message.decode('utf-8') if message else ""
            
            debug_message = DebugMessage(
                source=DebugSource(source),
                type=DebugType(msg_type),
                id=msg_id,
                severity=DebugSeverity(severity),
                message=msg_str
            )
            
            _user_debug_callback(debug_message)
        except Exception as e:
            print(f"Unhandled exception in OpenAL debug callback: {e}")

# Create a C-compatible function pointer from our Python handler.
# This must be kept alive globally.
_C_DEBUG_CALLBACK = al.ALDEBUGPROCEXT(_c_debug_callback_handler)


def set_debug_callback(callback):
    """
    Registers a callback function to receive OpenAL debug messages.

    The callback function may be invoked from a separate OpenAL thread.
    Ensure that any code within the callback is thread-safe.

    Args:
        callback (callable): A function that accepts a single argument (a
                             `DebugMessage` object). Pass `None` to unregister
                             the callback.
    """
    from ._internal import _ensure_context
    _ensure_context()
    global _user_debug_callback
    
    if callback is None:
        # Unregister the callback
        _user_debug_callback = None
        al.debug_message_callback_ext(al.ALDEBUGPROCEXT(0), None)
    else:
        if not callable(callback):
            raise TypeError("The provided callback must be a callable function or None.")
        
        _user_debug_callback = callback
        al.debug_message_callback_ext(_C_DEBUG_CALLBACK, None)

def control_debug_messages(source: DebugSource, msg_type: DebugType, severity: DebugSeverity, enable: bool, ids: list[int] = None):
    """
    Enables or disables notifications for a class of debug messages.

    Args:
        source (DebugSource): The source of the messages to control.
        msg_type (DebugType): The type of messages to control.
        severity (DebugSeverity): The severity level to control.
        enable (bool): Set to True to enable, False to disable.
        ids (list[int], optional): A list of specific message IDs to control.
                                   If None, all messages matching the other
                                   parameters will be affected.
    """

    from ._internal import _ensure_context
    _ensure_context()    
    id_array = None
    count = 0
    if ids is not None:
        count = len(ids)
        id_array = (ctypes.c_uint * count)(*ids)
    
    al.debug_message_control_ext(source.value, msg_type.value, severity.value, count, id_array, al.AL_TRUE if enable else al.AL_FALSE)


def insert_debug_message(source: DebugSource, msg_type: DebugType, severity: DebugSeverity, message: str, msg_id: int = 0):
    """
    Injects a custom message into the OpenAL debug log.

    This is useful for marking specific points in your application's code
    to correlate with OpenAL's own debug output.

    Args:
        source (DebugSource): The source to report, typically APPLICATION.
        msg_type (DebugType): The type of message, typically MARKER or OTHER.
        severity (DebugSeverity): The severity, typically NOTIFICATION.
        message (str): The debug message string to insert.
        msg_id (int, optional): An optional integer ID for the message.
    """
    from ._internal import _ensure_context
    _ensure_context()
    al.debug_message_insert_ext(source.value, msg_type.value, msg_id, severity.value, message)
