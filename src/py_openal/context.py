from . import alc
from .exceptions import OalError
from .listener import Listener

class Context:
    """An OpenAL context for a specific device."""

    def __init__(self, device, context_attr_list=None):
        """
        Creates a context on the given device.
        
        Args:
            device: An open PyOpenAL Device object.
        """
        if device.is_closed:
            raise OalError("Device must be open to create a context")
            
        self._context = alc.alcCreateContext(device._device, context_attr_list)
        if not self._context:
            raise OalError("Could not create context")
        
        self._as_parameter_ = self._context
        self._listener = Listener()

    @property
    def listener(self):
        """The listener for this context."""
        return self._listener
        
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
