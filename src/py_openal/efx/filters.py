import ctypes
import warnings
from abc import ABC, abstractmethod
from .. import al
from ..exceptions import OalError

class Filter(ABC):
    """Abstract base class for all EFX filter objects."""
    def __init__(self):
        self._id = ctypes.c_uint()
        al.alGenFilters(1, ctypes.byref(self._id))
        self._id_value = self._id.value
        al.alFilteri(self._id, al.AL_FILTER_TYPE, self._get_filter_type())

    @property
    def id(self):
        """The underlying OpenAL filter ID."""
        return self._id_value

    @abstractmethod
    def _get_filter_type(self):
        """Should be implemented by subclasses to return their AL_FILTER_* enum."""
        pass

    def __del__(self):
        if hasattr(self, '_id_value') and self._id_value is not None:
            warnings.warn(f"Orphaned Filter object (ID: {self._id_value}). "
                          "Please explicitly call .destroy() on EFX objects.",
                          ResourceWarning)

    def destroy(self):
        """Releases the OpenAL filter resource."""
        if self._id_value is not None:
            temp_id = (ctypes.c_uint * 1)(self._id_value)
            al.alDeleteFilters(1, temp_id)
            self._id_value = None
            
    def _set_float_property(self, param, value):
        if self._id_value is None:
            raise OalError("Filter has been destroyed.")
        al.alFilterf(self._id, param, float(value))

    def _get_float_property(self, param):
        if self._id_value is None:
            raise OalError("Filter has been destroyed.")
        value = ctypes.c_float()
        al.alGetFilterf(self._id, param, ctypes.byref(value))
        return value.value


class LowPassFilter(Filter):
    """A filter that passes low frequencies and attenuates high frequencies."""
    def _get_filter_type(self):
        return al.AL_FILTER_LOWPASS

    @property
    def gain(self):
        """The master volume of the direct signal. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_LOWPASS_GAIN)

    @gain.setter
    def gain(self, value):
        self._set_float_property(al.AL_LOWPASS_GAIN, value)

    @property
    def gainhf(self):
        """Attenuates high-frequencies. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_LOWPASS_GAINHF)

    @gainhf.setter
    def gainhf(self, value):
        self._set_float_property(al.AL_LOWPASS_GAINHF, value)


class HighPassFilter(Filter):
    """A filter that passes high frequencies and attenuates low frequencies."""
    def _get_filter_type(self):
        return al.AL_FILTER_HIGHPASS
        
    @property
    def gain(self):
        """The master volume of the direct signal. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_HIGHPASS_GAIN)

    @gain.setter
    def gain(self, value):
        self._set_float_property(al.AL_HIGHPASS_GAIN, value)

    @property
    def gainlf(self):
        """Attenuates low-frequencies. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_HIGHPASS_GAINLF)
        
    @gainlf.setter
    def gainlf(self, value):
        self._set_float_property(al.AL_HIGHPASS_GAINLF, value)


class BandPassFilter(Filter):
    """A filter that passes a specific range of frequencies."""
    def _get_filter_type(self):
        return al.AL_FILTER_BANDPASS

    @property
    def gain(self):
        """The master volume of the direct signal. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_BANDPASS_GAIN)

    @gain.setter
    def gain(self, value):
        self._set_float_property(al.AL_BANDPASS_GAIN, value)

    @property
    def gainlf(self):
        """Attenuates low-frequencies. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_BANDPASS_GAINLF)
        
    @gainlf.setter
    def gainlf(self, value):
        self._set_float_property(al.AL_BANDPASS_GAINLF, value)

    @property
    def gainhf(self):
        """Attenuates high-frequencies. Range [0.0, 1.0]."""
        return self._get_float_property(al.AL_BANDPASS_GAINHF)

    @gainhf.setter
    def gainhf(self, value):
        self._set_float_property(al.AL_BANDPASS_GAINHF, value)
