import ctypes
from .source import Source
from . import al
from .al import _get_al_ext_proc, ALint64SOFT
from ._internal import _ensure_context

def _operate_on_sources(source_list, operation_func):
    """
    Internal helper function to operate on a list of sources.

    Args:
        source_list (list[Source]): A list of Source objects.
        operation_func: The al.alSource...v function to call.
    """
    _ensure_context()
    if not source_list:
        return

    # Validate that all items are Source objects
    if not all(isinstance(s, Source) for s in source_list):
        raise TypeError("Input must be a list or tuple of Source objects.")

    num_sources = len(source_list)
    source_ids = (ctypes.c_uint * num_sources)(*[s.id for s in source_list])
    
    operation_func(num_sources, source_ids)

def play_sources(sources):
    """
    Plays a list of sources simultaneously (atomic operation).

    Args:
        sources (list[Source]): A list or tuple of Source objects to play.
    """
    _operate_on_sources(sources, al.alSourcePlayv)

def play_sources_at_time(sources, start_time: int):
    """
    Schedules a list of sources to play simultaneously at a specific time.
    Requires the AL_SOFT_source_start_delay extension.

    Args:
        sources (list[Source]): A list or tuple of Source objects to play.
        start_time (int): The absolute device clock time in nanoseconds.
    """
    _ensure_context()
    if not sources:
        return

    if not all(isinstance(s, Source) for s in sources):
        raise TypeError("Input must be a list or tuple of Source objects.")

    proc = _get_al_ext_proc(
        'alSourcePlayAtTimevSOFT',
        [ctypes.c_int, ctypes.POINTER(ctypes.c_uint), ALint64SOFT],
        None
    )

    num_sources = len(sources)
    source_ids = (ctypes.c_uint * num_sources)(*[s.id for s in sources])
    proc(num_sources, source_ids, start_time)

def stop_sources(sources):
    """
    Stops a list of sources simultaneously (atomic operation).

    Args:
        sources (list[Source]): A list or tuple of Source objects to stop.
    """
    _operate_on_sources(sources, al.alSourceStopv)

def pause_sources(sources):
    """
    Pauses a list of sources simultaneously (atomic operation).

    Args:
        sources (list[Source]): A list or tuple of Source objects to pause.
    """
    _operate_on_sources(sources, al.alSourcePausev)

def rewind_sources(sources):
    """

    Rewinds a list of sources simultaneously (atomic operation).

    Args:
        sources (list[Source]): A list or tuple of Source objects to rewind.
    """
    _operate_on_sources(sources, al.alSourceRewindv)

class SourcePool:
    """
    A high-level class for managing a group of Source objects.

    This class provides convenient methods for controlling multiple sources
    at once, including synchronized playback and broadcasting property changes.
    """
    def __init__(self, sources=None):
        """
        Initializes the SourcePool.

        Args:
            sources (list[Source], optional): An initial list of sources to manage.
        """
        if sources is None:
            self._sources = []
        else:
            if not all(isinstance(s, Source) for s in sources):
                raise TypeError("SourcePool can only be initialized with a list of Source objects.")
            self._sources = list(sources)

    def __len__(self):
        return len(self._sources)

    def __getitem__(self, index):
        return self._sources[index]

    def __iter__(self):
        return iter(self._sources)

    def add(self, source):
        """Adds a source to the pool."""
        if not isinstance(source, Source):
            raise TypeError("Can only add Source objects to the pool.")
        self._sources.append(source)


    def play_all(self):
        """Plays all sources in the pool simultaneously."""
        play_sources(self._sources)

    def play_all_at_time(self, start_time: int):
        """
        Schedules all sources in the pool to play simultaneously at a specific time.
        Requires the AL_SOFT_source_start_delay extension.

        Args:
            start_time (int): The absolute device clock time in nanoseconds.
        """
        play_sources_at_time(self._sources, start_time)

    def stop_all(self):
        """Stops all sources in the pool simultaneously."""
        stop_sources(self._sources)

    def pause_all(self):
        """Pauses all sources in the pool simultaneously."""
        pause_sources(self._sources)

    def rewind_all(self):
        """Rewinds all sources in the pool simultaneously."""
        rewind_sources(self._sources)

    def set_gain_all(self, gain):
        """Sets the gain for every source in the pool."""
        for source in self._sources:
            source.gain = gain

    def set_pitch_all(self, pitch):
        """Sets the pitch for every source in the pool."""
        for source in self._sources:
            source.pitch = pitch
            
    def set_looping_all(self, looping):
        """Sets the looping property for every source in the pool."""
        for source in self._sources:
            source.looping = looping

    def destroy(self):
        """
        Destroys all sources in the pool, releasing their OpenAL resources.
        The pool should not be used after calling this.
        """
        for source in self._sources:
            source.destroy()
        self._sources = []
