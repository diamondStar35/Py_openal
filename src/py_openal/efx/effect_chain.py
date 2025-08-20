import warnings
from .slot import EffectSlot
from .effect import Effect
from ..exceptions import OalError

class EffectChain:
    """
    A high-level utility for managing a chain of effects.

    This class simplifies the process of chaining multiple effects together by
    automatically creating and connecting the necessary EffectSlot objects.
    """
    def __init__(self, context, effects: list):
        """
        Creates an effect chain.

        Args:
            context (Context): The active context, used as a factory for slots.
            effects (list[Effect]): A list of pre-configured Effect objects,
                                    in the order they should be applied.
        """
        if not effects:
            raise ValueError("EffectChain requires at least one effect.")
        if not all(isinstance(e, Effect) for e in effects):
            raise TypeError("The 'effects' argument must be a list of Effect objects.")

        self._slots = []
        for i, effect in enumerate(effects):
            slot = context.create_effect_slot(effect)
            self._slots.append(slot)
            
            # If this is not the first slot, chain the previous one to this one
            if i > 0:
                self._slots[i-1].target = slot
        
        self._is_destroyed = False

    @property
    def input_slot(self) -> EffectSlot:
        """
        The first EffectSlot in the chain.
        
        Use this slot as the target for a source's auxiliary send to route
        its audio through the entire chain.
        """
        if self._is_destroyed:
            raise OalError("EffectChain has been destroyed.")
        return self._slots[0]

    @property
    def slots(self) -> list[EffectSlot]:
        """A list of all the EffectSlot objects managed by this chain."""
        if self._is_destroyed:
            raise OalError("EffectChain has been destroyed.")
        return self._slots

    def __getitem__(self, index) -> EffectSlot:
        """Allows accessing individual slots by index (e.g., chain[0])."""
        if self._is_destroyed:
            raise OalError("EffectChain has been destroyed.")
        return self._slots[index]

    def __len__(self) -> int:
        """Returns the number of effects (and slots) in the chain."""
        return len(self._slots)

    def destroy(self):
        """
        Destroys all EffectSlot objects managed by this chain.
        The chain should not be used after calling this.
        """
        if not self._is_destroyed:
            for slot in self._slots:
                slot.destroy()
            self._slots = []
            self._is_destroyed = True

    def __del__(self):
        if hasattr(self, '_is_destroyed') and not self._is_destroyed:
            warnings.warn("Orphaned EffectChain object. "
                          "Please explicitly call .destroy() on EffectChain objects.",
                          ResourceWarning)
