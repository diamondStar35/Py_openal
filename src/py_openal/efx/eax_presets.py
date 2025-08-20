"""
This module contains predefined effect settings for the EAXReverb effect,
ported from the efx-presets.h header in the OpenAL Soft SDK.

The keys are user-friendly names that can be passed to the 
EAXReverb.apply_preset() method.
"""

PRESETS = {
    "Generic": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.8913, 'gainlf': 1.0,
        'decay_time': 1.49, 'decay_hfratio': 0.83, 'decay_lfratio': 1.0,
        'reflections_gain': 0.05, 'reflections_delay': 0.007, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.2589, 'late_reverb_delay': 0.011, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Padded Cell": {
        'density': 0.1715, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.001, 'gainlf': 1.0,
        'decay_time': 0.17, 'decay_hfratio': 0.1, 'decay_lfratio': 1.0,
        'reflections_gain': 0.25, 'reflections_delay': 0.001, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.2691, 'late_reverb_delay': 0.002, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Room": {
        'density': 0.4287, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.5929, 'gainlf': 1.0,
        'decay_time': 0.4, 'decay_hfratio': 0.83, 'decay_lfratio': 1.0,
        'reflections_gain': 0.1503, 'reflections_delay': 0.002, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.0629, 'late_reverb_delay': 0.003, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Bathroom": {
        'density': 0.1715, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.2512, 'gainlf': 1.0,
        'decay_time': 1.49, 'decay_hfratio': 0.54, 'decay_lfratio': 1.0,
        'reflections_gain': 0.6531, 'reflections_delay': 0.007, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 3.2734, 'late_reverb_delay': 0.011, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Living Room": {
        'density': 0.9766, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.001, 'gainlf': 1.0,
        'decay_time': 0.5, 'decay_hfratio': 0.1, 'decay_lfratio': 1.0,
        'reflections_gain': 0.2051, 'reflections_delay': 0.003, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.2805, 'late_reverb_delay': 0.004, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Stone Room": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.7079, 'gainlf': 1.0,
        'decay_time': 2.31, 'decay_hfratio': 0.64, 'decay_lfratio': 1.0,
        'reflections_gain': 0.4411, 'reflections_delay': 0.012, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.1003, 'late_reverb_delay': 0.017, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Auditorium": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.5781, 'gainlf': 1.0,
        'decay_time': 4.32, 'decay_hfratio': 0.59, 'decay_lfratio': 1.0,
        'reflections_gain': 0.4032, 'reflections_delay': 0.02, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.717, 'late_reverb_delay': 0.03, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Concert Hall": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.5623, 'gainlf': 1.0,
        'decay_time': 3.92, 'decay_hfratio': 0.7, 'decay_lfratio': 1.0,
        'reflections_gain': 0.2427, 'reflections_delay': 0.02, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.9977, 'late_reverb_delay': 0.029, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Cave": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 1.0, 'gainlf': 1.0,
        'decay_time': 2.91, 'decay_hfratio': 1.3, 'decay_lfratio': 1.0,
        'reflections_gain': 0.5, 'reflections_delay': 0.015, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.7063, 'late_reverb_delay': 0.022, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Arena": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.4477, 'gainlf': 1.0,
        'decay_time': 7.24, 'decay_hfratio': 0.33, 'decay_lfratio': 1.0,
        'reflections_gain': 0.2612, 'reflections_delay': 0.02, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.0186, 'late_reverb_delay': 0.03, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Hangar": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.3162, 'gainlf': 1.0,
        'decay_time': 10.05, 'decay_hfratio': 0.23, 'decay_lfratio': 1.0,
        'reflections_gain': 0.5, 'reflections_delay': 0.02, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.256, 'late_reverb_delay': 0.03, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Carpeted Hallway": {
        'density': 0.4287, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.01, 'gainlf': 1.0,
        'decay_time': 0.3, 'decay_hfratio': 0.1, 'decay_lfratio': 1.0,
        'reflections_gain': 0.1215, 'reflections_delay': 0.002, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.1531, 'late_reverb_delay': 0.03, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Hallway": {
        'density': 0.3645, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.7079, 'gainlf': 1.0,
        'decay_time': 1.49, 'decay_hfratio': 0.59, 'decay_lfratio': 1.0,
        'reflections_gain': 0.2458, 'reflections_delay': 0.007, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.6615, 'late_reverb_delay': 0.011, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Stone Corridor": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.7612, 'gainlf': 1.0,
        'decay_time': 2.7, 'decay_hfratio': 0.79, 'decay_lfratio': 1.0,
        'reflections_gain': 0.2472, 'reflections_delay': 0.013, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.5758, 'late_reverb_delay': 0.02, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Alley": {
        'density': 1.0, 'diffusion': 0.3, 'gain': 0.3162, 'gainhf': 0.7328, 'gainlf': 1.0,
        'decay_time': 1.49, 'decay_hfratio': 0.86, 'decay_lfratio': 1.0,
        'reflections_gain': 0.25, 'reflections_delay': 0.007, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.9954, 'late_reverb_delay': 0.011, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.125, 'echo_depth': 0.95, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Forest": {
        'density': 1.0, 'diffusion': 0.3, 'gain': 0.3162, 'gainhf': 0.0224, 'gainlf': 1.0,
        'decay_time': 1.49, 'decay_hfratio': 0.54, 'decay_lfratio': 1.0,
        'reflections_gain': 0.0525, 'reflections_delay': 0.162, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.7682, 'late_reverb_delay': 0.088, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.125, 'echo_depth': 1.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "City": {
        'density': 1.0, 'diffusion': 0.5, 'gain': 0.3162, 'gainhf': 0.3981, 'gainlf': 1.0,
        'decay_time': 1.49, 'decay_hfratio': 0.67, 'decay_lfratio': 1.0,
        'reflections_gain': 0.073, 'reflections_delay': 0.007, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.1427, 'late_reverb_delay': 0.011, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Mountains": {
        'density': 1.0, 'diffusion': 0.27, 'gain': 0.3162, 'gainhf': 0.0562, 'gainlf': 1.0,
        'decay_time': 1.49, 'decay_hfratio': 0.21, 'decay_lfratio': 1.0,
        'reflections_gain': 0.0407, 'reflections_delay': 0.3, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.1919, 'late_reverb_delay': 0.1, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 1.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Quarry": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.3162, 'gainlf': 1.0,
        'decay_time': 1.49, 'decay_hfratio': 0.83, 'decay_lfratio': 1.0,
        'reflections_gain': 0.0, 'reflections_delay': 0.061, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.7783, 'late_reverb_delay': 0.025, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.125, 'echo_depth': 0.7, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Plain": {
        'density': 1.0, 'diffusion': 0.21, 'gain': 0.3162, 'gainhf': 0.1, 'gainlf': 1.0,
        'decay_time': 1.49, 'decay_hfratio': 0.5, 'decay_lfratio': 1.0,
        'reflections_gain': 0.0585, 'reflections_delay': 0.179, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.1089, 'late_reverb_delay': 0.1, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 1.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Parking Lot": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 1.0, 'gainlf': 1.0,
        'decay_time': 1.65, 'decay_hfratio': 1.5, 'decay_lfratio': 1.0,
        'reflections_gain': 0.2082, 'reflections_delay': 0.008, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.2652, 'late_reverb_delay': 0.012, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Sewer Pipe": {
        'density': 0.3071, 'diffusion': 0.8, 'gain': 0.3162, 'gainhf': 0.3162, 'gainlf': 1.0,
        'decay_time': 2.81, 'decay_hfratio': 0.14, 'decay_lfratio': 1.0,
        'reflections_gain': 1.6387, 'reflections_delay': 0.014, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 3.2471, 'late_reverb_delay': 0.021, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Underwater": {
        'density': 0.3645, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.01, 'gainlf': 1.0,
        'decay_time': 1.49, 'decay_hfratio': 0.1, 'decay_lfratio': 1.0,
        'reflections_gain': 0.5963, 'reflections_delay': 0.007, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 7.0795, 'late_reverb_delay': 0.011, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 1.18, 'modulation_depth': 0.348,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
}
