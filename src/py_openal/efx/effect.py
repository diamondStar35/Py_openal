import ctypes
import warnings
from abc import ABC, abstractmethod
from .. import al
from ..exceptions import OalError

class Effect(ABC):
    """
    Abstract base class for all EFX effect objects.
    """
    def __init__(self):
        self._id = ctypes.c_uint()
        al.alGenEffects(1, ctypes.byref(self._id))
        self._id_value = self._id.value
        # The first thing we must do is set the effect type.
        al.alEffecti(self._id, al.AL_EFFECT_TYPE, self._get_effect_type())

    @property
    def id(self):
        """The underlying OpenAL effect ID."""
        return self._id_value

    @abstractmethod
    def _get_effect_type(self):
        """Should be implemented by subclasses to return their AL_EFFECT_* enum."""
        pass

    def __del__(self):
        if hasattr(self, '_id_value') and self._id_value is not None:
            warnings.warn(f"Orphaned Effect object (ID: {self._id_value}). "
                          "Please explicitly call .destroy() on EFX objects.",
                          ResourceWarning)

    def destroy(self):
        """Releases the OpenAL effect resource."""
        if self._id_value is not None:
            temp_id = (ctypes.c_uint * 1)(self._id_value)
            al.alDeleteEffects(1, temp_id)
            self._id_value = None

    def _set_int_property(self, param, value):
        if self._id_value is None:
            raise OalError("Effect has been destroyed.")
        al.alEffecti(self._id, param, int(value))

    def _get_int_property(self, param):
        if self._id_value is None:
            raise OalError("Effect has been destroyed.")
        value = ctypes.c_int()
        al.alGetEffecti(self._id, param, ctypes.byref(value))
        return value.value

    def _set_float_property(self, param, value):
        if self._id_value is None:
            raise OalError("Effect has been destroyed.")
        al.alEffectf(self._id, param, float(value))

    def _get_float_property(self, param):
        if self._id_value is None:
            raise OalError("Effect has been destroyed.")
        value = ctypes.c_float()
        al.alGetEffectf(self._id, param, ctypes.byref(value))
        return value.value

    def _set_bool_property(self, param, value):
        if self._id_value is None:
            raise OalError("Effect has been destroyed.")
        al.alEffecti(self._id, param, al.AL_TRUE if value else al.AL_FALSE)

    def _get_bool_property(self, param):
        if self._id_value is None:
            raise OalError("Effect has been destroyed.")
        value = ctypes.c_int()
        al.alGetEffecti(self._id, param, ctypes.byref(value))
        return value.value == al.AL_TRUE

    def _set_vector_property(self, param, vec3):
        if self._id_value is None:
            raise OalError("Effect has been destroyed.")
        try:
            if len(vec3) != 3:
                raise ValueError("Vector property must have 3 elements (e.g., a tuple or list).")
        except TypeError:
            raise TypeError("Vector property must be a sequence (e.g., a tuple or list).")
        
        values = (ctypes.c_float * 3)(float(vec3[0]), float(vec3[1]), float(vec3[2]))
        al.alEffectfv(self._id, param, values)

    def _get_vector_property(self, param):
        if self._id_value is None:
            raise OalError("Effect has been destroyed.")
        values = (ctypes.c_float * 3)()
        al.alGetEffectfv(self._id, param, values)
        return tuple(values)
