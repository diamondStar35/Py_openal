import atexit
from . import device
from . import context
from . import alc

_default_device = None
_default_context = None

def _cleanup_context():
    """Function to be called at exit to clean up OpenAL resources."""
    global _default_device, _default_context
    
    # The context must be destroyed before the device is closed.
    if _default_context:
        # Note: Context.destroy() also calls alcMakeContextCurrent(None)
        _default_context.destroy()
        _default_context = None
        
    if _default_device:
        _default_device.close()
        _default_device = None

def _ensure_context():
    """
    Ensures that a default device and context are created and active.
    This is called by high-level functions like open() and stream().
    """
    global _default_device, _default_context
    
    # If a context hasn't been created yet, create one.
    if _default_context is None:
        try:
            device_name = device.get_default_device()
            _default_device = device.Device(device_name)
        except Exception:
            _default_device = device.Device()
            
        _default_context = context.Context(_default_device)
        _default_context.make_current()
        
        atexit.register(_cleanup_context)
