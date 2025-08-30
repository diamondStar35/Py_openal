"""
The EFX (Effects Extension) module for PyOpenAL.

This package contains classes for creating and managing audio effects,
filters, and the slots that hold them.
"""

from .slot import EffectSlot
from .effect_chain import EffectChain
from .filters import Filter, LowPassFilter, HighPassFilter, BandPassFilter

from .reverb import Reverb
from .eax_reverb import EAXReverb
from .chorus import Chorus
from .distortion import Distortion
from .echo import Echo
from .flanger import Flanger
from .frequency_shifter import FrequencyShifter
from .vocal_morpher import VocalMorpher
from .pitch_shifter import PitchShifter
from .ring_modulator import RingModulator
from .auto_wah import Autowah
from .compressor import Compressor
from .equalizer import Equalizer


__all__ = [
    'EffectSlot',
    'EffectChain',
    'LowPassFilter',
    'HighPassFilter',
    'BandPassFilter',
    'Reverb',
    'EAXReverb',
    'Chorus',
    'Distortion',
    'Echo',
    'Flanger',
    'FrequencyShifter',
    'VocalMorpher',
    'PitchShifter',
    'RingModulator',
    'Autowah',
    'Compressor',
    'Equalizer',
]