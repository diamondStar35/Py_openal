from .. import al
from .effect import Effect

class Echo(Effect):
    """
    The Echo effect generates discrete, delayed repetitions of the input signal.
    It can be used to create simple, single-bounce echoes or more complex,
    decaying echo patterns.
    """
    def _get_effect_type(self):
        return al.AL_EFFECT_ECHO

    @property
    def delay(self):
        """
        The primary delay time for the first echo, in seconds. 
        Range [0.0 to 0.207].
        
        This sets the fundamental timing of the echo repetitions. Default is 0.1s.
        """
        return self._get_float_property(al.AL_ECHO_DELAY)

    @delay.setter
    def delay(self, value):
        self._set_float_property(al.AL_ECHO_DELAY, value)

    @property
    def lrdelay(self):
        """
        The delay between the left and right channel echoes, in seconds.
        Range [0.0 to 0.404].
        
        A non-zero value creates a "ping-pong" effect, where echoes bounce
        between the stereo channels. This value is added to the main `delay`
        for the right channel. Default is 0.1s.
        """
        return self._get_float_property(al.AL_ECHO_LRDELAY)

    @lrdelay.setter
    def lrdelay(self, value):
        self._set_float_property(al.AL_ECHO_LRDELAY, value)

    @property
    def damping(self):
        """
        A factor controlling how much high-frequency content is attenuated
        with each subsequent echo. Range [0.0 to 0.99].
        
        A value of 0.0 means no damping, so echoes are bright. Higher values
        make each echo sound darker and more distant. Default is 0.5.
        """
        return self._get_float_property(al.AL_ECHO_DAMPING)

    @damping.setter
    def damping(self, value):
        self._set_float_property(al.AL_ECHO_DAMPING, value)

    @property
    def feedback(self):
        """
        The amount of the echo signal that is fed back into the input,
        controlling the number of repetitions. Range [0.0 to 1.0].
        
        A value of 0.0 will produce only a single echo. A value close to 1.0
        will create a long, slowly fading trail of echoes. Default is 0.5.
        """
        return self._get_float_property(al.AL_ECHO_FEEDBACK)

    @feedback.setter
    def feedback(self, value):
        self._set_float_property(al.AL_ECHO_FEEDBACK, value)

    @property
    def spread(self):
        """
        Controls the stereo panning of the echoes. Range [-1.0 to 1.0].
        
        A value of -1.0 pans all echoes to the left channel. A value of 1.0
        pans them to the right. 0.0 keeps them centered. Default is -1.0.
        """
        return self._get_float_property(al.AL_ECHO_SPREAD)

    @spread.setter
    def spread(self, value):
        self._set_float_property(al.AL_ECHO_SPREAD, value)
