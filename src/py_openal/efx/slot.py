import ctypes
import warnings
from .. import al
from ..exceptions import OalError

class EffectSlot:
    """
    Represents an Auxiliary Effect Slot, which can host a single Effect.
    
    Sources can be configured to send their audio signal to this slot
    to be processed with the loaded effect.
    """
    def __init__(self, effect=None):
        """
        Creates an Effect Slot.

        Args:
            effect (Effect, optional): An initial effect object to load into this slot.
        """
        self._id = ctypes.c_uint()
        al.alGenAuxiliaryEffectSlots(1, ctypes.byref(self._id))
        self._id_value = self._id.value
        self._effect = None
        self._target = None

        if effect:
            self.effect = effect

    @property
    def id(self):
        """The underlying OpenAL effect slot ID."""
        return self._id_value

    def __del__(self):
        if hasattr(self, '_id_value') and self._id_value is not None:
            warnings.warn(f"Orphaned EffectSlot object (ID: {self._id_value}). "
                          "Please explicitly call .destroy() on EFX objects.",
                          ResourceWarning)

    def destroy(self):
        """Releases the OpenAL effect slot resource."""
        if self._id_value is not None:
            # Detach any effect first
            self.effect = None
            temp_id = (ctypes.c_uint * 1)(self._id_value)
            al.alDeleteAuxiliaryEffectSlots(1, temp_id)
            self._id_value = None
            
    def _set_float_property(self, param, value):
        if self._id_value is None:
            raise OalError("EffectSlot has been destroyed.")
        al.alAuxiliaryEffectSlotf(self._id, param, float(value))

    def _get_float_property(self, param):
        if self._id_value is None:
            raise OalError("EffectSlot has been destroyed.")
        value = ctypes.c_float()
        al.alGetAuxiliaryEffectSlotf(self._id, param, ctypes.byref(value))
        return value.value

    def _set_bool_property(self, param, value):
        if self._id_value is None:
            raise OalError("EffectSlot has been destroyed.")
        al.alAuxiliaryEffectSloti(self._id, param, al.AL_TRUE if value else al.AL_FALSE)

    def _get_bool_property(self, param):
        if self._id_value is None:
            raise OalError("EffectSlot has been destroyed.")
        value = ctypes.c_int()
        al.alGetAuxiliaryEffectSloti(self._id, param, ctypes.byref(value))
        return value.value == al.AL_TRUE

    @property
    def gain(self):
        """The master gain for this effect slot. Range [0.0, 1.0]. Default 1.0."""
        return self._get_float_property(al.AL_EFFECTSLOT_GAIN)

    @gain.setter
    def gain(self, value):
        self._set_float_property(al.AL_EFFECTSLOT_GAIN, value)

    @property
    def target(self):
        """
        The target EffectSlot for this slot's output.
        Requires the AL_SOFT_effect_target extension.

        Set to another EffectSlot to chain effects, or None to send the
        output to the main mix.
        """
        return self._target

    @target.setter
    def target(self, target_slot):
        """
        Sets the output target for this effect slot.
        """
        if self._id_value is None:
            raise OalError("EffectSlot has been destroyed.")

        if target_slot is not None and not isinstance(target_slot, EffectSlot):
            raise TypeError("Target must be an EffectSlot instance or None.")

        target_id = target_slot.id if target_slot is not None else al.AL_EFFECTSLOT_NULL
        al.alAuxiliaryEffectSloti(self._id, al.AL_EFFECTSLOT_TARGET_SOFT, target_id)
        self._target = target_slot

    @property
    def auxiliary_send_auto(self):
        """
        Controls whether the send level from sources is automatically
        attenuated by distance. Boolean. Default is True.
        """
        return self._get_bool_property(al.AL_EFFECTSLOT_AUXILIARY_SEND_AUTO)

    @auxiliary_send_auto.setter
    def auxiliary_send_auto(self, value):
        self._set_bool_property(al.AL_EFFECTSLOT_AUXILIARY_SEND_AUTO, value)

    @property
    def effect(self):
        """The pyopenal.efx.Effect object loaded into this slot."""
        return self._effect

    @effect.setter
    def effect(self, effect_obj):
        """
        Loads an effect into the slot.
        
        Args:
            effect_obj: The effect to load, or None to clear the slot.
        """
        if self._id_value is None:
            raise OalError("EffectSlot has been destroyed.")
        
        effect_id = effect_obj.id if effect_obj is not None else al.AL_EFFECT_NULL
        al.alAuxiliaryEffectSloti(self._id, al.AL_EFFECTSLOT_EFFECT, effect_id)
        self._effect = effect_obj
