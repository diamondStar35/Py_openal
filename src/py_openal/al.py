import sys
import os
import ctypes
import ctypes.util
from .al_lib import lib


ALint64SOFT = ctypes.c_int64
AL_NONE = 0
AL_FALSE = 0
AL_TRUE = 1
AL_SOURCE_RELATIVE = 0x202
AL_CONE_INNER_ANGLE = 0x1001
AL_CONE_OUTER_ANGLE = 0x1002
AL_PITCH = 0x1003
AL_POSITION = 0x1004
AL_DIRECTION = 0x1005
AL_VELOCITY = 0x1006
AL_LOOPING = 0x1007
AL_BUFFER = 0x1009
AL_GAIN = 0x100A
AL_MIN_GAIN = 0x100D
AL_MAX_GAIN = 0x100E
AL_ORIENTATION = 0x100F
AL_SOURCE_STATE = 0x1010
AL_INITIAL = 0x1011
AL_PLAYING = 0x1012
AL_PAUSED = 0x1013
AL_STOPPED = 0x1014
AL_BUFFERS_QUEUED = 0x1015
AL_BUFFERS_PROCESSED = 0x1016
AL_SEC_OFFSET = 0x1024
AL_SAMPLE_OFFSET = 0x1025
AL_BYTE_OFFSET = 0x1026
AL_SOURCE_TYPE = 0x1027
AL_STATIC = 0x1028
AL_STREAMING = 0x1029
AL_UNDETERMINED = 0x1030
AL_FORMAT_MONO8 = 0x1100
AL_FORMAT_MONO16 = 0x1101
AL_FORMAT_STEREO8 = 0x1102
AL_FORMAT_STEREO16 = 0x1103
AL_FORMAT_MONO_FLOAT32 = 0x10010
AL_FORMAT_STEREO_FLOAT32 = 0x10011

# AL_EXT_double
AL_FORMAT_MONO_DOUBLE_EXT = 0x10012
AL_FORMAT_STEREO_DOUBLE_EXT = 0x10013

# AL_EXT_MULAW
AL_FORMAT_MONO_MULAW_EXT = 0x10014
AL_FORMAT_STEREO_MULAW_EXT = 0x10015

# AL_EXT_ALAW
AL_FORMAT_MONO_ALAW_EXT = 0x10016
AL_FORMAT_STEREO_ALAW_EXT = 0x10017

# AL_EXT_MCFORMATS - Multi-channel formats
AL_FORMAT_QUAD8 = 0x1204
AL_FORMAT_QUAD16 = 0x1205
AL_FORMAT_QUAD32 = 0x1206
AL_FORMAT_REAR8 = 0x1207
AL_FORMAT_REAR16 = 0x1208
AL_FORMAT_REAR32 = 0x1209
AL_FORMAT_51CHN8 = 0x120A
AL_FORMAT_51CHN16 = 0x120B
AL_FORMAT_51CHN32 = 0x120C
AL_FORMAT_61CHN8 = 0x120D
AL_FORMAT_61CHN16 = 0x120E
AL_FORMAT_61CHN32 = 0x120F
AL_FORMAT_71CHN8 = 0x1210
AL_FORMAT_71CHN16 = 0x1211
AL_FORMAT_71CHN32 = 0x1212

# AL_EXT_BFORMAT - Ambisonic formats
AL_FORMAT_BFORMAT2D_8 = 0x20021
AL_FORMAT_BFORMAT2D_16 = 0x20022
AL_FORMAT_BFORMAT2D_FLOAT32 = 0x20023
AL_FORMAT_BFORMAT3D_8 = 0x20031
AL_FORMAT_BFORMAT3D_16 = 0x20032
AL_FORMAT_BFORMAT3D_FLOAT32 = 0x20033

# AL_SOFT_UHJ - Ambisonic UHJ formats
AL_FORMAT_UHJ2CHN8_SOFT = 0x19A2
AL_FORMAT_UHJ2CHN16_SOFT = 0x19A3
AL_FORMAT_UHJ2CHN_FLOAT32_SOFT = 0x19A4
AL_FORMAT_UHJ3CHN8_SOFT = 0x19A5
AL_FORMAT_UHJ3CHN16_SOFT = 0x19A6
AL_FORMAT_UHJ3CHN_FLOAT32_SOFT = 0x19A7
AL_FORMAT_UHJ4CHN8_SOFT = 0x19A8
AL_FORMAT_UHJ4CHN16_SOFT = 0x19A9
AL_FORMAT_UHJ4CHN_FLOAT32_SOFT = 0x19AA

# AL_SOFT_source_spatialize
AL_SOURCE_SPATIALIZE_SOFT = 0x1214
AL_AUTO_SOFT = 0x0002
AL_REFERENCE_DISTANCE = 0x1020
AL_ROLLOFF_FACTOR = 0x1021
AL_CONE_OUTER_GAIN = 0x1022
AL_MAX_DISTANCE = 0x1023
AL_FREQUENCY = 0x2001
AL_BITS = 0x2002
AL_CHANNELS = 0x2003
AL_SIZE = 0x2004
AL_UNUSED = 0x2010
AL_PENDING = 0x2011
AL_PROCESSED = 0x2012
AL_NO_ERROR = AL_FALSE
AL_INVALID_NAME = 0xA001
AL_INVALID_ENUM = 0xA002
AL_INVALID_VALUE = 0xA003
AL_INVALID_OPERATION = 0xA004
AL_OUT_OF_MEMORY = 0xA005
AL_VENDOR = 0xB001
AL_VERSION = 0xB002
AL_RENDERER = 0xB003
AL_EXTENSIONS = 0xB004
AL_DOPPLER_FACTOR = 0xC000
AL_DOPPLER_VELOCITY = 0xC001
AL_SPEED_OF_SOUND = 0xC003
AL_DISTANCE_MODEL = 0xD000
AL_INVERSE_DISTANCE = 0xD001
AL_INVERSE_DISTANCE_CLAMPED = 0xD002
AL_LINEAR_DISTANCE = 0xD003
AL_LINEAR_DISTANCE_CLAMPED = 0xD004
AL_EXPONENT_DISTANCE = 0xD005
AL_EXPONENT_DISTANCE_CLAMPED = 0xD006
AL_SOURCE_DISTANCE_MODEL = 0x200
AL_DEFERRED_UPDATES_SOFT = 0xC002
AL_LOOP_POINTS_SOFT = 0x2015
AL_STEREO_ANGLES = 0x1030
AL_SOURCE_RADIUS = 0x1031
AL_DIRECT_CHANNELS_SOFT = 0x1033

# AL_SOFT_UHJ
AL_STEREO_MODE_SOFT = 0x19B0
AL_NORMAL_SOFT = 0x0000
AL_SUPER_STEREO_SOFT = 0x0001
AL_SUPER_STEREO_WIDTH_SOFT = 0x19B1

# AL_SOFT_direct_channels_remix
AL_DROP_UNMATCHED_SOFT = 0x0001
AL_REMIX_UNMATCHED_SOFT = 0x0002

# AL_SOFT_source_resampler
AL_NUM_RESAMPLERS_SOFT = 0x1210
AL_DEFAULT_RESAMPLER_SOFT = 0x1211
AL_SOURCE_RESAMPLER_SOFT = 0x1212
AL_RESAMPLER_NAME_SOFT = 0x1213

# AL_SOFT_buffer_samples
AL_MONO_SOFT = 0x1500
AL_STEREO_SOFT = 0x1501
AL_REAR_SOFT = 0x1502
AL_QUAD_SOFT = 0x1503
AL_5POINT1_SOFT = 0x1504
AL_6POINT1_SOFT = 0x1505
AL_7POINT1_SOFT = 0x1506
AL_BYTE_SOFT = 0x1400
AL_UNSIGNED_BYTE_SOFT = 0x1401
AL_SHORT_SOFT = 0x1402
AL_UNSIGNED_SHORT_SOFT = 0x1403
AL_INT_SOFT = 0x1404
AL_UNSIGNED_INT_SOFT = 0x1405
AL_FLOAT_SOFT = 0x1406
AL_DOUBLE_SOFT = 0x1407
AL_INTERNAL_FORMAT_SOFT = 0x2008
AL_BYTE_LENGTH_SOFT = 0x2009
AL_SAMPLE_LENGTH_SOFT = 0x200A
AL_SEC_LENGTH_SOFT = 0x200B

# AL_SOFT_source_latency
AL_SAMPLE_OFFSET_LATENCY_SOFT = 0x1200 # <-- ADD THIS LINE
AL_SEC_OFFSET_LATENCY_SOFT = 0x1201 # <-- ADD THIS LINE
AL_SAMPLE_OFFSET_CLOCK_SOFT = 0x1202
AL_SEC_OFFSET_CLOCK_SOFT = 0x1203

# HRTF related extensions
AL_STEREO_ANGLES = 0x1030

# Listener properties
AL_METERS_PER_UNIT = 0x20004

# Source properties
AL_DIRECT_FILTER = 0x20005
AL_AUXILIARY_SEND_FILTER = 0x20006
AL_AIR_ABSORPTION_FACTOR = 0x20007
AL_ROOM_ROLLOFF_FACTOR = 0x20008
AL_CONE_OUTER_GAINHF = 0x20009
AL_DIRECT_FILTER_GAINHF_AUTO = 0x2000A
AL_AUXILIARY_SEND_FILTER_GAIN_AUTO = 0x2000B
AL_AUXILIARY_SEND_FILTER_GAINHF_AUTO = 0x2000C

# Effect Slot object
AL_EFFECTSLOT_EFFECT = 0x0001
AL_EFFECTSLOT_GAIN = 0x0002
AL_EFFECTSLOT_AUXILIARY_SEND_AUTO = 0x0003
AL_EFFECTSLOT_NULL = 0x0000
AL_EFFECTSLOT_TARGET_SOFT = 0x199C

# Effect object
AL_EFFECT_TYPE = 0x8001
AL_EFFECT_NULL = 0x0000

# Effect Types
AL_EFFECT_REVERB = 0x0001
AL_EFFECT_CHORUS = 0x0002
AL_EFFECT_DISTORTION = 0x0003
AL_EFFECT_ECHO = 0x0004
AL_EFFECT_FLANGER = 0x0005
AL_EFFECT_FREQUENCY_SHIFTER = 0x0006
AL_EFFECT_VOCAL_MORPHER = 0x0007
AL_EFFECT_PITCH_SHIFTER = 0x0008
AL_EFFECT_RING_MODULATOR = 0x0009
AL_EFFECT_AUTOWAH = 0x000A
AL_EFFECT_COMPRESSOR = 0x000B
AL_EFFECT_EQUALIZER = 0x000C
AL_EFFECT_EAXREVERB = 0x8000

# Reverb Effect Parameters
AL_REVERB_DENSITY = 0x0001
AL_REVERB_DIFFUSION = 0x0002
AL_REVERB_GAIN = 0x0003
AL_REVERB_GAINHF = 0x0004
AL_REVERB_DECAY_TIME = 0x0005
AL_REVERB_DECAY_HFRATIO = 0x0006
AL_REVERB_REFLECTIONS_GAIN = 0x0007
AL_REVERB_REFLECTIONS_DELAY = 0x0008
AL_REVERB_LATE_REVERB_GAIN = 0x0009
AL_REVERB_LATE_REVERB_DELAY = 0x000A
AL_REVERB_AIR_ABSORPTION_GAINHF = 0x000B
AL_REVERB_ROOM_ROLLOFF_FACTOR = 0x000C
AL_REVERB_DECAY_HFLIMIT = 0x000D

# EAX Reverb Effect Parameters
AL_EAXREVERB_DENSITY = 0x0001
AL_EAXREVERB_DIFFUSION = 0x0002
AL_EAXREVERB_GAIN = 0x0003
AL_EAXREVERB_GAINHF = 0x0004
AL_EAXREVERB_GAINLF = 0x0005
AL_EAXREVERB_DECAY_TIME = 0x0006
AL_EAXREVERB_DECAY_HFRATIO = 0x0007
AL_EAXREVERB_DECAY_LFRATIO = 0x0008
AL_EAXREVERB_REFLECTIONS_GAIN = 0x0009
AL_EAXREVERB_REFLECTIONS_DELAY = 0x000A
AL_EAXREVERB_REFLECTIONS_PAN = 0x000B
AL_EAXREVERB_LATE_REVERB_GAIN = 0x000C
AL_EAXREVERB_LATE_REVERB_DELAY = 0x000D
AL_EAXREVERB_LATE_REVERB_PAN = 0x000E
AL_EAXREVERB_ECHO_TIME = 0x000F
AL_EAXREVERB_ECHO_DEPTH = 0x0010
AL_EAXREVERB_MODULATION_TIME = 0x0011
AL_EAXREVERB_MODULATION_DEPTH = 0x0012
AL_EAXREVERB_AIR_ABSORPTION_GAINHF = 0x0013
AL_EAXREVERB_HFREFERENCE = 0x0014
AL_EAXREVERB_LFREFERENCE = 0x0015
AL_EAXREVERB_ROOM_ROLLOFF_FACTOR = 0x0016
AL_EAXREVERB_DECAY_HFLIMIT = 0x0017

# Chorus Effect Parameters
AL_CHORUS_WAVEFORM = 0x0001
AL_CHORUS_PHASE = 0x0002
AL_CHORUS_RATE = 0x0003
AL_CHORUS_DEPTH = 0x0004
AL_CHORUS_FEEDBACK = 0x0005
AL_CHORUS_DELAY = 0x0006

# Distortion Effect Parameters
AL_DISTORTION_EDGE = 0x0001
AL_DISTORTION_GAIN = 0x0002
AL_DISTORTION_LOWPASS_CUTOFF = 0x0003
AL_DISTORTION_EQCENTER = 0x0004
AL_DISTORTION_EQBANDWIDTH = 0x0005

# Echo Effect Parameters
AL_ECHO_DELAY = 0x0001
AL_ECHO_LRDELAY = 0x0002
AL_ECHO_DAMPING = 0x0003
AL_ECHO_FEEDBACK = 0x0004
AL_ECHO_SPREAD = 0x0005

# Flanger Effect Parameters
AL_FLANGER_WAVEFORM = 0x0001
AL_FLANGER_PHASE = 0x0002
AL_FLANGER_RATE = 0x0003
AL_FLANGER_DEPTH = 0x0004
AL_FLANGER_FEEDBACK = 0x0005
AL_FLANGER_DELAY = 0x0006

# Frequency Shifter Effect Parameters
AL_FREQUENCY_SHIFTER_FREQUENCY = 0x0001
AL_FREQUENCY_SHIFTER_LEFT_DIRECTION = 0x0002
AL_FREQUENCY_SHIFTER_RIGHT_DIRECTION = 0x0003

# Vocal Morpher Effect Parameters
AL_VOCAL_MORPHER_PHONEMEA = 0x0001
AL_VOCAL_MORPHER_PHONEMEA_COARSE_TUNING = 0x0002
AL_VOCAL_MORPHER_PHONEMEB = 0x0003
AL_VOCAL_MORPHER_PHONEMEB_COARSE_TUNING = 0x0004
AL_VOCAL_MORPHER_WAVEFORM = 0x0005
AL_VOCAL_MORPHER_RATE = 0x0006

# Pitch Shifter Effect Parameters
AL_PITCH_SHIFTER_COARSE_TUNE = 0x0001
AL_PITCH_SHIFTER_FINE_TUNE = 0x0002

# Ring Modulator Effect Parameters
AL_RING_MODULATOR_FREQUENCY = 0x0001
AL_RING_MODULATOR_HIGHPASS_CUTOFF = 0x0002
AL_RING_MODULATOR_WAVEFORM = 0x0003

# Compressor Effect Parameters
AL_COMPRESSOR_ONOFF = 0x0001

# Equalizer Effect Parameters
AL_EQUALIZER_LOW_GAIN = 0x0001
AL_EQUALIZER_LOW_CUTOFF = 0x0002
AL_EQUALIZER_MID1_GAIN = 0x0003
AL_EQUALIZER_MID1_CENTER = 0x0004
AL_EQUALIZER_MID1_WIDTH = 0x0005
AL_EQUALIZER_MID2_GAIN = 0x0006
AL_EQUALIZER_MID2_CENTER = 0x0007
AL_EQUALIZER_MID2_WIDTH = 0x0008
AL_EQUALIZER_HIGH_GAIN = 0x0009
AL_EQUALIZER_HIGH_CUTOFF = 0x000A

# Filter object
AL_FILTER_TYPE = 0x8001
AL_FILTER_NULL = 0x0000

# Filter Types
AL_FILTER_LOWPASS = 0x0001
AL_FILTER_HIGHPASS = 0x0002
AL_FILTER_BANDPASS = 0x0003

# Lowpass Filter Parameters
AL_LOWPASS_GAIN = 0x0001
AL_LOWPASS_GAINHF = 0x0002

# Highpass Filter Parameters
AL_HIGHPASS_GAIN = 0x0001
AL_HIGHPASS_GAINLF = 0x0002

# Bandpass Filter Parameters
AL_BANDPASS_GAIN = 0x0001
AL_BANDPASS_GAINLF = 0x0002
AL_BANDPASS_GAINHF = 0x0003

# AL_SOFT_events
AL_EVENT_CALLBACK_FUNCTION_SOFT = 0x19A2
AL_EVENT_CALLBACK_USER_PARAM_SOFT = 0x19A3
AL_EVENT_TYPE_BUFFER_COMPLETED_SOFT = 0x19A4
AL_EVENT_TYPE_SOURCE_STATE_CHANGED_SOFT = 0x19A5
AL_EVENT_TYPE_DISCONNECTED_SOFT = 0x19A6

# AL_EXT_debug
AL_DONT_CARE_EXT = 0x0002
AL_DEBUG_OUTPUT_EXT = 0x19B2
AL_DEBUG_CALLBACK_FUNCTION_EXT = 0x19B3
AL_DEBUG_CALLBACK_USER_PARAM_EXT = 0x19B4
AL_DEBUG_SOURCE_API_EXT = 0x19B5
AL_DEBUG_SOURCE_AUDIO_SYSTEM_EXT = 0x19B6
AL_DEBUG_SOURCE_THIRD_PARTY_EXT = 0x19B7
AL_DEBUG_SOURCE_APPLICATION_EXT = 0x19B8
AL_DEBUG_SOURCE_OTHER_EXT = 0x19B9
AL_DEBUG_TYPE_ERROR_EXT = 0x19BA
AL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_EXT = 0x19BB
AL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_EXT = 0x19BC
AL_DEBUG_TYPE_PORTABILITY_EXT = 0x19BD
AL_DEBUG_TYPE_PERFORMANCE_EXT = 0x19BE
AL_DEBUG_TYPE_MARKER_EXT = 0x19BF
AL_DEBUG_TYPE_PUSH_GROUP_EXT = 0x19C0
AL_DEBUG_TYPE_POP_GROUP_EXT = 0x19C1
AL_DEBUG_TYPE_OTHER_EXT = 0x19C2
AL_DEBUG_SEVERITY_HIGH_EXT = 0x19C3
AL_DEBUG_SEVERITY_MEDIUM_EXT = 0x19C4
AL_DEBUG_SEVERITY_LOW_EXT = 0x19C5
AL_DEBUG_SEVERITY_NOTIFICATION_EXT = 0x19C6

al_enums = {}
local_items = list(locals().items())
for k, v in local_items:
    if type(v) != int: continue
    if not v in al_enums:
        al_enums[v] = []
    al_enums[v].append(k)

class ALError(Exception):
    pass

_al_ext_procs = {}
def _get_al_ext_proc(func_name, argtypes, restype):
    """Internal helper to load and cache AL extension functions."""
    if func_name in _al_ext_procs:
        return _al_ext_procs[func_name]
    
    # alGetProcAddress requires a current context to be active.
    # It's assumed this is called by a high-level function that ensures this.
    func_ptr = alGetProcAddress(func_name.encode('utf-8'))
    if not func_ptr:
        raise OalError(f"AL extension function '{func_name}' not supported.")
        
    cfunc = ctypes.CFUNCTYPE(restype, *argtypes)(func_ptr)
    if func_name != 'alGetStringiSOFT':
        cfunc.errcheck = al_check_error
    _al_ext_procs[func_name] = cfunc
    return cfunc

alGetError = lib.alGetError
alGetError.argtypes = []
alGetError.restype = ctypes.c_int

def al_check_error(result, func, arguments):
    err = alGetError()
    if err:
        raise ALError(al_enums[err][0])
    return result

alEnable = lib.alEnable
alEnable.argtypes = [ctypes.c_int]
alEnable.restype = None
alEnable.errcheck = al_check_error

alDisable = lib.alDisable
alDisable.argtypes = [ctypes.c_int]
alDisable.restype = None
alDisable.errcheck = al_check_error

alIsEnabled = lib.alIsEnabled
alIsEnabled.argtypes = [ctypes.c_int]
alIsEnabled.restype = ctypes.c_uint8
alIsEnabled.errcheck = al_check_error

alGetString = lib.alGetString
alGetString.argtypes = [ctypes.c_int]
alGetString.restype = ctypes.c_void_p
alGetString.errcheck = al_check_error

alGetBooleanv = lib.alGetBooleanv
alGetBooleanv.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint8)]
alGetBooleanv.restype = None
alGetBooleanv.errcheck = al_check_error

alGetIntegerv = lib.alGetIntegerv
alGetIntegerv.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alGetIntegerv.restype = None
alGetIntegerv.errcheck = al_check_error

alGetFloatv = lib.alGetFloatv
alGetFloatv.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alGetFloatv.restype = None
alGetFloatv.errcheck = al_check_error

alGetDoublev = lib.alGetDoublev
alGetDoublev.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
alGetDoublev.restype = None
alGetDoublev.errcheck = al_check_error

alGetBoolean = lib.alGetBoolean
alGetBoolean.argtypes = [ctypes.c_int]
alGetBoolean.restype = ctypes.c_uint8
alGetBoolean.errcheck = al_check_error

alGetInteger = lib.alGetInteger
alGetInteger.argtypes = [ctypes.c_int]
alGetInteger.restype = ctypes.c_int
alGetInteger.errcheck = al_check_error

alGetFloat = lib.alGetFloat
alGetFloat.argtypes = [ctypes.c_int]
alGetFloat.restype = ctypes.c_float
alGetFloat.errcheck = al_check_error

alGetDouble = lib.alGetDouble
alGetDouble.argtypes = [ctypes.c_int]
alGetDouble.restype = ctypes.c_double
alGetDouble.errcheck = al_check_error



alIsExtensionPresent = lib.alIsExtensionPresent
alIsExtensionPresent.argtypes = [ctypes.c_char_p]
alIsExtensionPresent.restype = ctypes.c_uint8
alIsExtensionPresent.errcheck = al_check_error

alGetProcAddress = lib.alGetProcAddress
alGetProcAddress.argtypes = [ctypes.c_char_p]
alGetProcAddress.restype = ctypes.c_void_p
alGetProcAddress.errcheck = al_check_error

alGetEnumValue = lib.alGetEnumValue
alGetEnumValue.argtypes = [ctypes.c_char_p]
alGetEnumValue.restype = ctypes.c_int
alGetEnumValue.errcheck = al_check_error

alListenerf = lib.alListenerf
alListenerf.argtypes = [ctypes.c_int, ctypes.c_float]
alListenerf.restype = None
alListenerf.errcheck = al_check_error

alListener3f = lib.alListener3f
alListener3f.argtypes = [ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float]
alListener3f.restype = None
alListener3f.errcheck = al_check_error

alListenerfv = lib.alListenerfv
alListenerfv.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alListenerfv.restype = None
alListenerfv.errcheck = al_check_error

alListeneri = lib.alListeneri
alListeneri.argtypes = [ctypes.c_int, ctypes.c_int]
alListeneri.restype = None
alListeneri.errcheck = al_check_error

alListener3i = lib.alListener3i
alListener3i.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
alListener3i.restype = None
alListener3i.errcheck = al_check_error

alListeneriv = lib.alListeneriv
alListeneriv.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alListeneriv.restype = None
alListeneriv.errcheck = al_check_error

alGetListenerf = lib.alGetListenerf
alGetListenerf.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alGetListenerf.restype = None
alGetListenerf.errcheck = al_check_error

alGetListener3f = lib.alGetListener3f
alGetListener3f.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]
alGetListener3f.restype = None
alGetListener3f.errcheck = al_check_error

alGetListenerfv = lib.alGetListenerfv
alGetListenerfv.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alGetListenerfv.restype = None
alGetListenerfv.errcheck = al_check_error

alGetListeneri = lib.alGetListeneri
alGetListeneri.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alGetListeneri.restype = None
alGetListeneri.errcheck = al_check_error

alGetListener3i = lib.alGetListener3i
alGetListener3i.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
alGetListener3i.restype = None
alGetListener3i.errcheck = al_check_error

alGetListeneriv = lib.alGetListeneriv
alGetListeneriv.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alGetListeneriv.restype = None
alGetListeneriv.errcheck = al_check_error

alGenSources = lib.alGenSources
alGenSources.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alGenSources.restype = None
alGenSources.errcheck = al_check_error

alDeleteSources = lib.alDeleteSources
alDeleteSources.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alDeleteSources.restype = None
alDeleteSources.errcheck = al_check_error

alIsSource = lib.alIsSource
alIsSource.argtypes = [ctypes.c_uint]
alIsSource.restype = ctypes.c_uint8
alIsSource.errcheck = al_check_error

alSourcef = lib.alSourcef
alSourcef.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_float]
alSourcef.restype = None
alSourcef.errcheck = al_check_error

alSource3f = lib.alSource3f
alSource3f.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float]
alSource3f.restype = None
alSource3f.errcheck = al_check_error

alSourcefv = lib.alSourcefv
alSourcefv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alSourcefv.restype = None
alSourcefv.errcheck = al_check_error

alSourcei = lib.alSourcei
alSourcei.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_int]
alSourcei.restype = None
alSourcei.errcheck = al_check_error

alSource3i = lib.alSource3i
alSource3i.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
alSource3i.restype = None
alSource3i.errcheck = al_check_error

alSourceiv = lib.alSourceiv
alSourceiv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alSourceiv.restype = None
alSourceiv.errcheck = al_check_error

alGetSourcef = lib.alGetSourcef
alGetSourcef.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alGetSourcef.restype = None
alGetSourcef.errcheck = al_check_error

alGetSource3f = lib.alGetSource3f
alGetSource3f.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]
alGetSource3f.restype = None
alGetSource3f.errcheck = al_check_error

alGetSourcefv = lib.alGetSourcefv
alGetSourcefv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alGetSourcefv.restype = None
alGetSourcefv.errcheck = al_check_error

alGetSourcei = lib.alGetSourcei
alGetSourcei.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alGetSourcei.restype = None
alGetSourcei.errcheck = al_check_error

alGetSource3i = lib.alGetSource3i
alGetSource3i.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
alGetSource3i.restype = None
alGetSource3i.errcheck = al_check_error

alGetSourceiv = lib.alGetSourceiv
alGetSourceiv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alGetSourceiv.restype = None
alGetSourceiv.errcheck = al_check_error

alSourcePlayv = lib.alSourcePlayv
alSourcePlayv.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alSourcePlayv.restype = None
alSourcePlayv.errcheck = al_check_error

alSourceStopv = lib.alSourceStopv
alSourceStopv.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alSourceStopv.restype = None
alSourceStopv.errcheck = al_check_error

alSourceRewindv = lib.alSourceRewindv
alSourceRewindv.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alSourceRewindv.restype = None
alSourceRewindv.errcheck = al_check_error

alSourcePausev = lib.alSourcePausev
alSourcePausev.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alSourcePausev.restype = None
alSourcePausev.errcheck = al_check_error

alSourcePlay = lib.alSourcePlay
alSourcePlay.argtypes = [ctypes.c_uint]
alSourcePlay.restype = None
alSourcePlay.errcheck = al_check_error

alSourceStop = lib.alSourceStop
alSourceStop.argtypes = [ctypes.c_uint]
alSourceStop.restype = None
alSourceStop.errcheck = al_check_error

alSourceRewind = lib.alSourceRewind
alSourceRewind.argtypes = [ctypes.c_uint]
alSourceRewind.restype = None
alSourceRewind.errcheck = al_check_error

alSourcePause = lib.alSourcePause
alSourcePause.argtypes = [ctypes.c_uint]
alSourcePause.restype = None
alSourcePause.errcheck = al_check_error

alSourceQueueBuffers = lib.alSourceQueueBuffers
alSourceQueueBuffers.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alSourceQueueBuffers.restype = None
alSourceQueueBuffers.errcheck = al_check_error

alSourceUnqueueBuffers = lib.alSourceUnqueueBuffers
alSourceUnqueueBuffers.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alSourceUnqueueBuffers.restype = None
alSourceUnqueueBuffers.errcheck = al_check_error

alGenBuffers = lib.alGenBuffers
alGenBuffers.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alGenBuffers.restype = None
alGenBuffers.errcheck = al_check_error

alDeleteBuffers = lib.alDeleteBuffers
alDeleteBuffers.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alDeleteBuffers.restype = None
alDeleteBuffers.errcheck = al_check_error

alIsBuffer = lib.alIsBuffer
alIsBuffer.argtypes = [ctypes.c_uint]
alIsBuffer.restype = ctypes.c_uint8
alIsBuffer.errcheck = al_check_error

alBufferData = lib.alBufferData
alBufferData.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
alBufferData.restype = None
alBufferData.errcheck = al_check_error

alBufferf = lib.alBufferf
alBufferf.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_float]
alBufferf.restype = None
alBufferf.errcheck = al_check_error

alBuffer3f = lib.alBuffer3f
alBuffer3f.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_float, ctypes.c_float, ctypes.c_float]
alBuffer3f.restype = None
alBuffer3f.errcheck = al_check_error

alBufferfv = lib.alBufferfv
alBufferfv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alBufferfv.restype = None
alBufferfv.errcheck = al_check_error

alBufferi = lib.alBufferi
alBufferi.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_int]
alBufferi.restype = None
alBufferi.errcheck = al_check_error

alBuffer3i = lib.alBuffer3i
alBuffer3i.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
alBuffer3i.restype = None
alBuffer3i.errcheck = al_check_error

alBufferiv = lib.alBufferiv
alBufferiv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alBufferiv.restype = None
alBufferiv.errcheck = al_check_error

alGetBufferf = lib.alGetBufferf
alGetBufferf.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alGetBufferf.restype = None
alGetBufferf.errcheck = al_check_error

alGetBuffer3f = lib.alGetBuffer3f
alGetBuffer3f.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)]
alGetBuffer3f.restype = None
alGetBuffer3f.errcheck = al_check_error

alGetBufferfv = lib.alGetBufferfv
alGetBufferfv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alGetBufferfv.restype = None
alGetBufferfv.errcheck = al_check_error

alGetBufferi = lib.alGetBufferi
alGetBufferi.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alGetBufferi.restype = None
alGetBufferi.errcheck = al_check_error

alGetBuffer3i = lib.alGetBuffer3i
alGetBuffer3i.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
alGetBuffer3i.restype = None
alGetBuffer3i.errcheck = al_check_error

alGetBufferiv = lib.alGetBufferiv
alGetBufferiv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alGetBufferiv.restype = None
alGetBufferiv.errcheck = al_check_error

alDopplerFactor = lib.alDopplerFactor
alDopplerFactor.argtypes = [ctypes.c_float]
alDopplerFactor.restype = None
alDopplerFactor.errcheck = al_check_error

alDopplerVelocity = lib.alDopplerVelocity
alDopplerVelocity.argtypes = [ctypes.c_float]
alDopplerVelocity.restype = None
alDopplerVelocity.errcheck = al_check_error

alSpeedOfSound = lib.alSpeedOfSound
alSpeedOfSound.argtypes = [ctypes.c_float]
alSpeedOfSound.restype = None
alSpeedOfSound.errcheck = al_check_error

alDistanceModel = lib.alDistanceModel
alDistanceModel.argtypes = [ctypes.c_int]
alDistanceModel.restype = None
alDistanceModel.errcheck = al_check_error

alDeferUpdatesSOFT = lib.alDeferUpdatesSOFT
alDeferUpdatesSOFT.argtypes = []
alDeferUpdatesSOFT.restype = None
alDeferUpdatesSOFT.errcheck = al_check_error

alProcessUpdatesSOFT = lib.alProcessUpdatesSOFT
alProcessUpdatesSOFT.argtypes = []
alProcessUpdatesSOFT.restype = None
alProcessUpdatesSOFT.errcheck = al_check_error

alIsBufferFormatSupportedSOFT = lib.alIsBufferFormatSupportedSOFT
alIsBufferFormatSupportedSOFT.argtypes = [ctypes.c_int] # ALenum
alIsBufferFormatSupportedSOFT.restype = ctypes.c_uint8 # ALboolean
alIsBufferFormatSupportedSOFT.errcheck = al_check_error

alBufferSamplesSOFT = lib.alBufferSamplesSOFT
alBufferSamplesSOFT.argtypes = [ctypes.c_uint, ctypes.c_uint, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_void_p]
alBufferSamplesSOFT.restype = None
alBufferSamplesSOFT.errcheck = al_check_error

alBufferSubDataSOFT = lib.alBufferSubDataSOFT
alBufferSubDataSOFT.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
alBufferSubDataSOFT.restype = None
alBufferSubDataSOFT.errcheck = al_check_error

# Effect objects
alGenEffects = lib.alGenEffects
alGenEffects.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alGenEffects.restype = None
alGenEffects.errcheck = al_check_error

alDeleteEffects = lib.alDeleteEffects
alDeleteEffects.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alDeleteEffects.restype = None
alDeleteEffects.errcheck = al_check_error

alIsEffect = lib.alIsEffect
alIsEffect.argtypes = [ctypes.c_uint]
alIsEffect.restype = ctypes.c_uint8
alIsEffect.errcheck = al_check_error

alEffecti = lib.alEffecti
alEffecti.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_int]
alEffecti.restype = None
alEffecti.errcheck = al_check_error

alEffectiv = lib.alEffectiv
alEffectiv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alEffectiv.restype = None
alEffectiv.errcheck = al_check_error

alEffectf = lib.alEffectf
alEffectf.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_float]
alEffectf.restype = None
alEffectf.errcheck = al_check_error

alEffectfv = lib.alEffectfv
alEffectfv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alEffectfv.restype = None
alEffectfv.errcheck = al_check_error

alGetEffecti = lib.alGetEffecti
alGetEffecti.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alGetEffecti.restype = None
alGetEffecti.errcheck = al_check_error

alGetEffectiv = lib.alGetEffectiv
alGetEffectiv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alGetEffectiv.restype = None
alGetEffectiv.errcheck = al_check_error

alGetEffectf = lib.alGetEffectf
alGetEffectf.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alGetEffectf.restype = None
alGetEffectf.errcheck = al_check_error

alGetEffectfv = lib.alGetEffectfv
alGetEffectfv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alGetEffectfv.restype = None
alGetEffectfv.errcheck = al_check_error

# Auxiliary Effect Slot objects
alGenAuxiliaryEffectSlots = lib.alGenAuxiliaryEffectSlots
alGenAuxiliaryEffectSlots.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alGenAuxiliaryEffectSlots.restype = None
alGenAuxiliaryEffectSlots.errcheck = al_check_error

alDeleteAuxiliaryEffectSlots = lib.alDeleteAuxiliaryEffectSlots
alDeleteAuxiliaryEffectSlots.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alDeleteAuxiliaryEffectSlots.restype = None
alDeleteAuxiliaryEffectSlots.errcheck = al_check_error

alIsAuxiliaryEffectSlot = lib.alIsAuxiliaryEffectSlot
alIsAuxiliaryEffectSlot.argtypes = [ctypes.c_uint]
alIsAuxiliaryEffectSlot.restype = ctypes.c_uint8
alIsAuxiliaryEffectSlot.errcheck = al_check_error

alAuxiliaryEffectSloti = lib.alAuxiliaryEffectSloti
alAuxiliaryEffectSloti.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_int]
alAuxiliaryEffectSloti.restype = None
alAuxiliaryEffectSloti.errcheck = al_check_error

alAuxiliaryEffectSlotiv = lib.alAuxiliaryEffectSlotiv
alAuxiliaryEffectSlotiv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alAuxiliaryEffectSlotiv.restype = None
alAuxiliaryEffectSlotiv.errcheck = al_check_error

alAuxiliaryEffectSlotf = lib.alAuxiliaryEffectSlotf
alAuxiliaryEffectSlotf.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_float]
alAuxiliaryEffectSlotf.restype = None
alAuxiliaryEffectSlotf.errcheck = al_check_error

alAuxiliaryEffectSlotfv = lib.alAuxiliaryEffectSlotfv
alAuxiliaryEffectSlotfv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alAuxiliaryEffectSlotfv.restype = None
alAuxiliaryEffectSlotfv.errcheck = al_check_error

alGetAuxiliaryEffectSloti = lib.alGetAuxiliaryEffectSloti
alGetAuxiliaryEffectSloti.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alGetAuxiliaryEffectSloti.restype = None
alGetAuxiliaryEffectSloti.errcheck = al_check_error

alGetAuxiliaryEffectSlotiv = lib.alGetAuxiliaryEffectSlotiv
alGetAuxiliaryEffectSlotiv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alGetAuxiliaryEffectSlotiv.restype = None
alGetAuxiliaryEffectSlotiv.errcheck = al_check_error

alGetAuxiliaryEffectSlotf = lib.alGetAuxiliaryEffectSlotf
alGetAuxiliaryEffectSlotf.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alGetAuxiliaryEffectSlotf.restype = None
alGetAuxiliaryEffectSlotf.errcheck = al_check_error

alGetAuxiliaryEffectSlotfv = lib.alGetAuxiliaryEffectSlotfv
alGetAuxiliaryEffectSlotfv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alGetAuxiliaryEffectSlotfv.restype = None
alGetAuxiliaryEffectSlotfv.errcheck = al_check_error

# Filter objects
alGenFilters = lib.alGenFilters
alGenFilters.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alGenFilters.restype = None
alGenFilters.errcheck = al_check_error

alDeleteFilters = lib.alDeleteFilters
alDeleteFilters.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_uint)]
alDeleteFilters.restype = None
alDeleteFilters.errcheck = al_check_error

alIsFilter = lib.alIsFilter
alIsFilter.argtypes = [ctypes.c_uint]
alIsFilter.restype = ctypes.c_uint8
alIsFilter.errcheck = al_check_error

alFilteri = lib.alFilteri
alFilteri.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_int]
alFilteri.restype = None
alFilteri.errcheck = al_check_error

alFilteriv = lib.alFilteriv
alFilteriv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alFilteriv.restype = None
alFilteriv.errcheck = al_check_error

alFilterf = lib.alFilterf
alFilterf.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.c_float]
alFilterf.restype = None
alFilterf.errcheck = al_check_error

alFilterfv = lib.alFilterfv
alFilterfv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alFilterfv.restype = None
alFilterfv.errcheck = al_check_error

alGetFilteri = lib.alGetFilteri
alGetFilteri.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alGetFilteri.restype = None
alGetFilteri.errcheck = al_check_error

alGetFilteriv = lib.alGetFilteriv
alGetFilteriv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_int)]
alGetFilteriv.restype = None
alGetFilteriv.errcheck = al_check_error

alGetFilterf = lib.alGetFilterf
alGetFilterf.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alGetFilterf.restype = None
alGetFilterf.errcheck = al_check_error

alGetFilterfv = lib.alGetFilterfv
alGetFilterfv.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_float)]
alGetFilterfv.restype = None
alGetFilterfv.errcheck = al_check_error

alGetSourcei64vSOFT = lib.alGetSourcei64vSOFT
alGetSourcei64vSOFT.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ALint64SOFT)]
alGetSourcei64vSOFT.restype = None
alGetSourcei64vSOFT.errcheck = al_check_error

alGetSourcedvSOFT = lib.alGetSourcedvSOFT
alGetSourcedvSOFT.argtypes = [ctypes.c_uint, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
alGetSourcedvSOFT.restype = None
alGetSourcedvSOFT.errcheck = al_check_error

# AL_EXT_debug
ALDEBUGPROCEXT = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_uint,
                                  ctypes.c_int, ctypes.c_int, ctypes.c_char_p,
                                  ctypes.c_void_p)

def debug_message_callback_ext(callback, user_param):
    proc = _get_al_ext_proc('alDebugMessageCallbackEXT', [ALDEBUGPROCEXT, ctypes.c_void_p], None)
    proc.errcheck = None # This function should not have an error check
    proc(callback, user_param)

def debug_message_control_ext(source, msg_type, severity, count, ids, enable):
    proc = _get_al_ext_proc('alDebugMessageControlEXT',
                            [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                             ctypes.POINTER(ctypes.c_uint), ctypes.c_uint8],
                            None)
    proc(source, msg_type, severity, count, ids, enable)

def debug_message_insert_ext(source, msg_type, msg_id, severity, message):
    encoded_msg = message.encode('utf-8')
    proc = _get_al_ext_proc('alDebugMessageInsertEXT',
                            [ctypes.c_int, ctypes.c_int, ctypes.c_uint,
                             ctypes.c_int, ctypes.c_int, ctypes.c_char_p],
                            None)
    proc(source, msg_type, msg_id, severity, len(encoded_msg), encoded_msg)

# AL_SOFT_events
ALEVENTPROCSOFT = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_uint, ctypes.c_uint,
                                  ctypes.c_int, ctypes.c_char_p, ctypes.c_void_p)

alEventControlSOFT = lib.alEventControlSOFT
alEventControlSOFT.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.c_uint8]
alEventControlSOFT.restype = None
alEventControlSOFT.errcheck = al_check_error

alEventCallbackSOFT = lib.alEventCallbackSOFT
alEventCallbackSOFT.argtypes = [ALEVENTPROCSOFT, ctypes.c_void_p]
alEventCallbackSOFT.restype = None
alEventCallbackSOFT.errcheck = al_check_error

