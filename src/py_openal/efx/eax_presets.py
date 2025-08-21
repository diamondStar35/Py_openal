"""
This module contains predefined effect settings for the EAXReverb effect,
ported from the efx-presets.h header in the OpenAL Soft SDK.

The keys are user-friendly names that can be passed to the 
EAXReverb.apply_preset() method.
"""

PRESETS = {
    # Default Presets
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
    "Drugged": {
        'density': 0.4287, 'diffusion': 0.5, 'gain': 0.3162, 'gainhf': 1.0, 'gainlf': 1.0,
        'decay_time': 8.39, 'decay_hfratio': 1.39, 'decay_lfratio': 1.0,
        'reflections_gain': 0.876, 'reflections_delay': 0.002, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 3.1081, 'late_reverb_delay': 0.03, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 1.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Dizzy": {
        'density': 0.3645, 'diffusion': 0.6, 'gain': 0.3162, 'gainhf': 0.631, 'gainlf': 1.0,
        'decay_time': 17.23, 'decay_hfratio': 0.56, 'decay_lfratio': 1.0,
        'reflections_gain': 0.1392, 'reflections_delay': 0.02, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.4937, 'late_reverb_delay': 0.03, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 1.0, 'modulation_time': 0.81, 'modulation_depth': 0.31,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Psychotic": {
        'density': 0.0625, 'diffusion': 0.5, 'gain': 0.3162, 'gainhf': 0.8404, 'gainlf': 1.0,
        'decay_time': 7.56, 'decay_hfratio': 0.91, 'decay_lfratio': 1.0,
        'reflections_gain': 0.4864, 'reflections_delay': 0.02, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 2.4378, 'late_reverb_delay': 0.03, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 4.0, 'modulation_depth': 1.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },

    # Castle Presets
    "Castle Small Room": {
        'density': 1.0, 'diffusion': 0.89, 'gain': 0.3162, 'gainhf': 0.3981, 'gainlf': 0.1,
        'decay_time': 1.22, 'decay_hfratio': 0.83, 'decay_lfratio': 0.31,
        'reflections_gain': 0.8913, 'reflections_delay': 0.022, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.9953, 'late_reverb_delay': 0.011, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.138, 'echo_depth': 0.08, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5168.6, 'lfreference': 139.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Castle Short Passage": {
        'density': 1.0, 'diffusion': 0.89, 'gain': 0.3162, 'gainhf': 0.3162, 'gainlf': 0.1,
        'decay_time': 2.32, 'decay_hfratio': 0.83, 'decay_lfratio': 0.31,
        'reflections_gain': 0.8913, 'reflections_delay': 0.007, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.2589, 'late_reverb_delay': 0.023, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.138, 'echo_depth': 0.08, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5168.6, 'lfreference': 139.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Castle Medium Room": {
        'density': 1.0, 'diffusion': 0.93, 'gain': 0.3162, 'gainhf': 0.2818, 'gainlf': 0.1,
        'decay_time': 2.04, 'decay_hfratio': 0.83, 'decay_lfratio': 0.46,
        'reflections_gain': 0.631, 'reflections_delay': 0.022, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.5849, 'late_reverb_delay': 0.011, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.155, 'echo_depth': 0.03, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5168.6, 'lfreference': 139.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Castle Large Room": {
        'density': 1.0, 'diffusion': 0.82, 'gain': 0.3162, 'gainhf': 0.2818, 'gainlf': 0.1259,
        'decay_time': 2.53, 'decay_hfratio': 0.83, 'decay_lfratio': 0.5,
        'reflections_gain': 0.4467, 'reflections_delay': 0.034, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.2589, 'late_reverb_delay': 0.016, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.185, 'echo_depth': 0.07, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5168.6, 'lfreference': 139.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Castle Long Passage": {
        'density': 1.0, 'diffusion': 0.89, 'gain': 0.3162, 'gainhf': 0.3981, 'gainlf': 0.1,
        'decay_time': 3.42, 'decay_hfratio': 0.83, 'decay_lfratio': 0.31,
        'reflections_gain': 0.8913, 'reflections_delay': 0.007, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.4125, 'late_reverb_delay': 0.023, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.138, 'echo_depth': 0.08, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5168.6, 'lfreference': 139.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Castle Hall": {
        'density': 1.0, 'diffusion': 0.81, 'gain': 0.3162, 'gainhf': 0.2818, 'gainlf': 0.1778,
        'decay_time': 3.14, 'decay_hfratio': 0.79, 'decay_lfratio': 0.62,
        'reflections_gain': 0.1778, 'reflections_delay': 0.056, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.122, 'late_reverb_delay': 0.024, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5168.6, 'lfreference': 139.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Castle Cupboard": {
        'density': 1.0, 'diffusion': 0.89, 'gain': 0.3162, 'gainhf': 0.2818, 'gainlf': 0.1,
        'decay_time': 0.67, 'decay_hfratio': 0.87, 'decay_lfratio': 0.31,
        'reflections_gain': 1.4125, 'reflections_delay': 0.01, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 3.5481, 'late_reverb_delay': 0.007, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.138, 'echo_depth': 0.08, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5168.6, 'lfreference': 139.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Castle Courtyard": {
        'density': 1.0, 'diffusion': 0.42, 'gain': 0.3162, 'gainhf': 0.4467, 'gainlf': 0.1995,
        'decay_time': 2.13, 'decay_hfratio': 0.61, 'decay_lfratio': 0.23,
        'reflections_gain': 0.2239, 'reflections_delay': 0.16, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.7079, 'late_reverb_delay': 0.036, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.37, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Castle Alcove": {
        'density': 1.0, 'diffusion': 0.89, 'gain': 0.3162, 'gainhf': 0.5012, 'gainlf': 0.1,
        'decay_time': 1.64, 'decay_hfratio': 0.87, 'decay_lfratio': 0.31,
        'reflections_gain': 1.0, 'reflections_delay': 0.007, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.4125, 'late_reverb_delay': 0.034, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.138, 'echo_depth': 0.08, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5168.6, 'lfreference': 139.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },

    # Factory Presets
    "Factory Small Room": {
        'density': 0.3645, 'diffusion': 0.82, 'gain': 0.3162, 'gainhf': 0.7943, 'gainlf': 0.5012,
        'decay_time': 1.72, 'decay_hfratio': 0.65, 'decay_lfratio': 1.31,
        'reflections_gain': 0.7079, 'reflections_delay': 0.01, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.7783, 'late_reverb_delay': 0.024, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.119, 'echo_depth': 0.07, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3762.6, 'lfreference': 362.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Factory Short Passage": {
        'density': 0.3645, 'diffusion': 0.64, 'gain': 0.2512, 'gainhf': 0.7943, 'gainlf': 0.5012,
        'decay_time': 2.53, 'decay_hfratio': 0.65, 'decay_lfratio': 1.31,
        'reflections_gain': 1.0, 'reflections_delay': 0.01, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.2589, 'late_reverb_delay': 0.038, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.135, 'echo_depth': 0.23, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3762.6, 'lfreference': 362.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Factory Medium Room": {
        'density': 0.4287, 'diffusion': 0.82, 'gain': 0.2512, 'gainhf': 0.7943, 'gainlf': 0.5012,
        'decay_time': 2.76, 'decay_hfratio': 0.65, 'decay_lfratio': 1.31,
        'reflections_gain': 0.2818, 'reflections_delay': 0.022, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.4125, 'late_reverb_delay': 0.023, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.174, 'echo_depth': 0.07, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3762.6, 'lfreference': 362.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Factory Large Room": {
        'density': 0.4287, 'diffusion': 0.75, 'gain': 0.2512, 'gainhf': 0.7079, 'gainlf': 0.631,
        'decay_time': 4.24, 'decay_hfratio': 0.51, 'decay_lfratio': 1.31,
        'reflections_gain': 0.1778, 'reflections_delay': 0.039, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.122, 'late_reverb_delay': 0.023, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.231, 'echo_depth': 0.07, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3762.6, 'lfreference': 362.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Factory Long Passage": {
        'density': 0.3645, 'diffusion': 0.64, 'gain': 0.2512, 'gainhf': 0.7943, 'gainlf': 0.5012,
        'decay_time': 4.06, 'decay_hfratio': 0.65, 'decay_lfratio': 1.31,
        'reflections_gain': 1.0, 'reflections_delay': 0.02, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.2589, 'late_reverb_delay': 0.037, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.135, 'echo_depth': 0.23, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3762.6, 'lfreference': 362.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Factory Hall": {
        'density': 0.4287, 'diffusion': 0.75, 'gain': 0.3162, 'gainhf': 0.7079, 'gainlf': 0.631,
        'decay_time': 7.43, 'decay_hfratio': 0.51, 'decay_lfratio': 1.31,
        'reflections_gain': 0.0631, 'reflections_delay': 0.073, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.8913, 'late_reverb_delay': 0.027, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.07, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3762.6, 'lfreference': 362.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Factory Cupboard": {
        'density': 0.3071, 'diffusion': 0.63, 'gain': 0.2512, 'gainhf': 0.7943, 'gainlf': 0.5012,
        'decay_time': 0.49, 'decay_hfratio': 0.65, 'decay_lfratio': 1.31,
        'reflections_gain': 1.2589, 'reflections_delay': 0.01, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.9953, 'late_reverb_delay': 0.032, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.107, 'echo_depth': 0.07, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3762.6, 'lfreference': 362.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Factory Courtyard": {
        'density': 0.3071, 'diffusion': 0.57, 'gain': 0.3162, 'gainhf': 0.3162, 'gainlf': 0.631,
        'decay_time': 2.32, 'decay_hfratio': 0.29, 'decay_lfratio': 0.56,
        'reflections_gain': 0.2239, 'reflections_delay': 0.14, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.3981, 'late_reverb_delay': 0.039, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.29, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3762.6, 'lfreference': 362.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Factory Alcove": {
        'density': 0.3645, 'diffusion': 0.59, 'gain': 0.2512, 'gainhf': 0.7943, 'gainlf': 0.5012,
        'decay_time': 3.14, 'decay_hfratio': 0.65, 'decay_lfratio': 1.31,
        'reflections_gain': 1.4125, 'reflections_delay': 0.01, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.0, 'late_reverb_delay': 0.038, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.114, 'echo_depth': 0.1, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3762.6, 'lfreference': 362.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },

    # Ice Palace Presets
    "Ice Palace Small Room": {
        'density': 1.0, 'diffusion': 0.84, 'gain': 0.3162, 'gainhf': 0.5623, 'gainlf': 0.2818,
        'decay_time': 1.51, 'decay_hfratio': 1.53, 'decay_lfratio': 0.27,
        'reflections_gain': 0.8913, 'reflections_delay': 0.01, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.4125, 'late_reverb_delay': 0.011, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.164, 'echo_depth': 0.14, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 12428.5, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Ice Palace Short Passage": {
        'density': 1.0, 'diffusion': 0.75, 'gain': 0.3162, 'gainhf': 0.5623, 'gainlf': 0.2818,
        'decay_time': 1.79, 'decay_hfratio': 1.46, 'decay_lfratio': 0.28,
        'reflections_gain': 0.5012, 'reflections_delay': 0.01, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.122, 'late_reverb_delay': 0.019, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.177, 'echo_depth': 0.09, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 12428.5, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Ice Palace Medium Room": {
        'density': 1.0, 'diffusion': 0.87, 'gain': 0.3162, 'gainhf': 0.5623, 'gainlf': 0.4467,
        'decay_time': 2.22, 'decay_hfratio': 1.53, 'decay_lfratio': 0.32,
        'reflections_gain': 0.3981, 'reflections_delay': 0.039, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.122, 'late_reverb_delay': 0.027, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.186, 'echo_depth': 0.12, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 12428.5, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Ice Palace Large Room": {
        'density': 1.0, 'diffusion': 0.81, 'gain': 0.3162, 'gainhf': 0.5623, 'gainlf': 0.4467,
        'decay_time': 3.14, 'decay_hfratio': 1.53, 'decay_lfratio': 0.32,
        'reflections_gain': 0.2512, 'reflections_delay': 0.039, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.0, 'late_reverb_delay': 0.027, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.214, 'echo_depth': 0.11, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 12428.5, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Ice Palace Long Passage": {
        'density': 1.0, 'diffusion': 0.77, 'gain': 0.3162, 'gainhf': 0.5623, 'gainlf': 0.3981,
        'decay_time': 3.01, 'decay_hfratio': 1.46, 'decay_lfratio': 0.28,
        'reflections_gain': 0.7943, 'reflections_delay': 0.012, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.2589, 'late_reverb_delay': 0.025, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.186, 'echo_depth': 0.04, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 12428.5, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Ice Palace Hall": {
        'density': 1.0, 'diffusion': 0.76, 'gain': 0.3162, 'gainhf': 0.4467, 'gainlf': 0.5623,
        'decay_time': 5.49, 'decay_hfratio': 1.53, 'decay_lfratio': 0.38,
        'reflections_gain': 0.1122, 'reflections_delay': 0.054, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.631, 'late_reverb_delay': 0.052, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.226, 'echo_depth': 0.11, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 12428.5, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Ice Palace Cupboard": {
        'density': 1.0, 'diffusion': 0.83, 'gain': 0.3162, 'gainhf': 0.5012, 'gainlf': 0.2239,
        'decay_time': 0.76, 'decay_hfratio': 1.53, 'decay_lfratio': 0.26,
        'reflections_gain': 1.122, 'reflections_delay': 0.012, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.9953, 'late_reverb_delay': 0.016, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.143, 'echo_depth': 0.08, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 12428.5, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Ice Palace Courtyard": {
        'density': 1.0, 'diffusion': 0.59, 'gain': 0.3162, 'gainhf': 0.2818, 'gainlf': 0.3162,
        'decay_time': 2.04, 'decay_hfratio': 1.2, 'decay_lfratio': 0.38,
        'reflections_gain': 0.3162, 'reflections_delay': 0.173, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.3162, 'late_reverb_delay': 0.043, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.235, 'echo_depth': 0.48, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 12428.5, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Ice Palace Alcove": {
        'density': 1.0, 'diffusion': 0.84, 'gain': 0.3162, 'gainhf': 0.5623, 'gainlf': 0.2818,
        'decay_time': 2.76, 'decay_hfratio': 1.46, 'decay_lfratio': 0.28,
        'reflections_gain': 1.122, 'reflections_delay': 0.01, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.8913, 'late_reverb_delay': 0.03, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.161, 'echo_depth': 0.09, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 12428.5, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },

    # Space Station Presets
    "Space Station Small Room": {
        'density': 0.2109, 'diffusion': 0.7, 'gain': 0.3162, 'gainhf': 0.7079, 'gainlf': 0.8913,
        'decay_time': 1.72, 'decay_hfratio': 0.82, 'decay_lfratio': 0.55,
        'reflections_gain': 0.7943, 'reflections_delay': 0.007, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.4125, 'late_reverb_delay': 0.013, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.188, 'echo_depth': 0.26, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3316.1, 'lfreference': 458.2,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Space Station Short Passage": {
        'density': 0.2109, 'diffusion': 0.87, 'gain': 0.3162, 'gainhf': 0.631, 'gainlf': 0.8913,
        'decay_time': 3.57, 'decay_hfratio': 0.5, 'decay_lfratio': 0.55,
        'reflections_gain': 1.0, 'reflections_delay': 0.012, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.122, 'late_reverb_delay': 0.016, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.172, 'echo_depth': 0.2, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3316.1, 'lfreference': 458.2,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Space Station Medium Room": {
        'density': 0.2109, 'diffusion': 0.75, 'gain': 0.3162, 'gainhf': 0.631, 'gainlf': 0.8913,
        'decay_time': 3.01, 'decay_hfratio': 0.5, 'decay_lfratio': 0.55,
        'reflections_gain': 0.3981, 'reflections_delay': 0.034, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.122, 'late_reverb_delay': 0.035, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.209, 'echo_depth': 0.31, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3316.1, 'lfreference': 458.2,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Space Station Large Room": {
        'density': 0.3645, 'diffusion': 0.81, 'gain': 0.3162, 'gainhf': 0.631, 'gainlf': 0.8913,
        'decay_time': 3.89, 'decay_hfratio': 0.38, 'decay_lfratio': 0.61,
        'reflections_gain': 0.3162, 'reflections_delay': 0.056, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.8913, 'late_reverb_delay': 0.035, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.233, 'echo_depth': 0.28, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3316.1, 'lfreference': 458.2,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Space Station Long Passage": {
        'density': 0.4287, 'diffusion': 0.82, 'gain': 0.3162, 'gainhf': 0.631, 'gainlf': 0.8913,
        'decay_time': 4.62, 'decay_hfratio': 0.62, 'decay_lfratio': 0.55,
        'reflections_gain': 1.0, 'reflections_delay': 0.012, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.2589, 'late_reverb_delay': 0.031, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.23, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3316.1, 'lfreference': 458.2,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Space Station Hall": {
        'density': 0.4287, 'diffusion': 0.87, 'gain': 0.3162, 'gainhf': 0.631, 'gainlf': 0.8913,
        'decay_time': 7.11, 'decay_hfratio': 0.38, 'decay_lfratio': 0.61,
        'reflections_gain': 0.1778, 'reflections_delay': 0.1, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.631, 'late_reverb_delay': 0.047, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.25, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3316.1, 'lfreference': 458.2,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Space Station Cupboard": {
        'density': 0.1715, 'diffusion': 0.56, 'gain': 0.3162, 'gainhf': 0.7079, 'gainlf': 0.8913,
        'decay_time': 0.79, 'decay_hfratio': 0.81, 'decay_lfratio': 0.55,
        'reflections_gain': 1.4125, 'reflections_delay': 0.007, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.7783, 'late_reverb_delay': 0.018, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.181, 'echo_depth': 0.31, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3316.1, 'lfreference': 458.2,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Space Station Alcove": {
        'density': 0.2109, 'diffusion': 0.78, 'gain': 0.3162, 'gainhf': 0.7079, 'gainlf': 0.8913,
        'decay_time': 1.16, 'decay_hfratio': 0.81, 'decay_lfratio': 0.55,
        'reflections_gain': 1.4125, 'reflections_delay': 0.007, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.0, 'late_reverb_delay': 0.018, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.192, 'echo_depth': 0.21, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 3316.1, 'lfreference': 458.2,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },

    # Wooden Galleon Presets
    "Wooden Small Room": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.1122, 'gainlf': 0.3162,
        'decay_time': 0.79, 'decay_hfratio': 0.32, 'decay_lfratio': 0.87,
        'reflections_gain': 1.0, 'reflections_delay': 0.032, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.8913, 'late_reverb_delay': 0.029, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 4705.0, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Wooden Short Passage": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.1259, 'gainlf': 0.3162,
        'decay_time': 1.75, 'decay_hfratio': 0.5, 'decay_lfratio': 0.87,
        'reflections_gain': 0.8913, 'reflections_delay': 0.012, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.631, 'late_reverb_delay': 0.024, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 4705.0, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Wooden Medium Room": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.1, 'gainlf': 0.2818,
        'decay_time': 1.47, 'decay_hfratio': 0.42, 'decay_lfratio': 0.82,
        'reflections_gain': 0.8913, 'reflections_delay': 0.049, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.8913, 'late_reverb_delay': 0.029, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 4705.0, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Wooden Large Room": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.0891, 'gainlf': 0.2818,
        'decay_time': 2.65, 'decay_hfratio': 0.33, 'decay_lfratio': 0.82,
        'reflections_gain': 0.8913, 'reflections_delay': 0.066, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.7943, 'late_reverb_delay': 0.049, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 4705.0, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Wooden Long Passage": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.1, 'gainlf': 0.3162,
        'decay_time': 1.99, 'decay_hfratio': 0.4, 'decay_lfratio': 0.79,
        'reflections_gain': 1.0, 'reflections_delay': 0.02, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.4467, 'late_reverb_delay': 0.036, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 4705.0, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Wooden Hall": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.0794, 'gainlf': 0.2818,
        'decay_time': 3.45, 'decay_hfratio': 0.3, 'decay_lfratio': 0.82,
        'reflections_gain': 0.8913, 'reflections_delay': 0.088, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.7943, 'late_reverb_delay': 0.063, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 4705.0, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Wooden Cupboard": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.1413, 'gainlf': 0.3162,
        'decay_time': 0.56, 'decay_hfratio': 0.46, 'decay_lfratio': 0.91,
        'reflections_gain': 1.122, 'reflections_delay': 0.012, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.122, 'late_reverb_delay': 0.028, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 4705.0, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Wooden Courtyard": {
        'density': 1.0, 'diffusion': 0.65, 'gain': 0.3162, 'gainhf': 0.0794, 'gainlf': 0.3162,
        'decay_time': 1.79, 'decay_hfratio': 0.35, 'decay_lfratio': 0.79,
        'reflections_gain': 0.5623, 'reflections_delay': 0.123, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.1, 'late_reverb_delay': 0.032, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 4705.0, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Wooden Alcove": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.1259, 'gainlf': 0.3162,
        'decay_time': 1.22, 'decay_hfratio': 0.62, 'decay_lfratio': 0.91,
        'reflections_gain': 1.122, 'reflections_delay': 0.012, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.7079, 'late_reverb_delay': 0.024, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 4705.0, 'lfreference': 99.6,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },

    # Sports Presets
    "Sport Empty Stadium": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.4467, 'gainlf': 0.7943,
        'decay_time': 6.26, 'decay_hfratio': 0.51, 'decay_lfratio': 1.1,
        'reflections_gain': 0.0631, 'reflections_delay': 0.183, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.3981, 'late_reverb_delay': 0.038, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Sport Squash Court": {
        'density': 1.0, 'diffusion': 0.75, 'gain': 0.3162, 'gainhf': 0.3162, 'gainlf': 0.7943,
        'decay_time': 2.22, 'decay_hfratio': 0.91, 'decay_lfratio': 1.16,
        'reflections_gain': 0.4467, 'reflections_delay': 0.007, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.7943, 'late_reverb_delay': 0.011, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.126, 'echo_depth': 0.19, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 7176.9, 'lfreference': 211.2,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Sport Small Swimming Pool": {
        'density': 1.0, 'diffusion': 0.7, 'gain': 0.3162, 'gainhf': 0.7943, 'gainlf': 0.8913,
        'decay_time': 2.76, 'decay_hfratio': 1.25, 'decay_lfratio': 1.14,
        'reflections_gain': 0.631, 'reflections_delay': 0.02, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.7943, 'late_reverb_delay': 0.03, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.179, 'echo_depth': 0.15, 'modulation_time': 0.895, 'modulation_depth': 0.19,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Sport Large Swimming Pool": {
        'density': 1.0, 'diffusion': 0.82, 'gain': 0.3162, 'gainhf': 0.7943, 'gainlf': 1.0,
        'decay_time': 5.49, 'decay_hfratio': 1.31, 'decay_lfratio': 1.14,
        'reflections_gain': 0.4467, 'reflections_delay': 0.039, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.5012, 'late_reverb_delay': 0.049, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.222, 'echo_depth': 0.55, 'modulation_time': 1.159, 'modulation_depth': 0.21,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Sport Gymnasium": {
        'density': 1.0, 'diffusion': 0.81, 'gain': 0.3162, 'gainhf': 0.4467, 'gainlf': 0.8913,
        'decay_time': 3.14, 'decay_hfratio': 1.06, 'decay_lfratio': 1.35,
        'reflections_gain': 0.3981, 'reflections_delay': 0.029, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.5623, 'late_reverb_delay': 0.045, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.146, 'echo_depth': 0.14, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 7176.9, 'lfreference': 211.2,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Sport Full Stadium": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.0708, 'gainlf': 0.7943,
        'decay_time': 5.25, 'decay_hfratio': 0.17, 'decay_lfratio': 0.8,
        'reflections_gain': 0.1, 'reflections_delay': 0.188, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.2818, 'late_reverb_delay': 0.038, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Sport Stadium Tannoy": {
        'density': 1.0, 'diffusion': 0.78, 'gain': 0.3162, 'gainhf': 0.5623, 'gainlf': 0.5012,
        'decay_time': 2.53, 'decay_hfratio': 0.88, 'decay_lfratio': 0.68,
        'reflections_gain': 0.2818, 'reflections_delay': 0.23, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.5012, 'late_reverb_delay': 0.063, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.2, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },

    # Prefab Presets
    "Prefab Workshop": {
        'density': 0.4287, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.1413, 'gainlf': 0.3981,
        'decay_time': 0.76, 'decay_hfratio': 1.0, 'decay_lfratio': 1.0,
        'reflections_gain': 1.0, 'reflections_delay': 0.012, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.122, 'late_reverb_delay': 0.012, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Prefab School Room": {
        'density': 0.4022, 'diffusion': 0.69, 'gain': 0.3162, 'gainhf': 0.631, 'gainlf': 0.5012,
        'decay_time': 0.98, 'decay_hfratio': 0.45, 'decay_lfratio': 0.18,
        'reflections_gain': 1.4125, 'reflections_delay': 0.017, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.4125, 'late_reverb_delay': 0.015, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.095, 'echo_depth': 0.14, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 7176.9, 'lfreference': 211.2,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Prefab Practise Room": {
        'density': 0.4022, 'diffusion': 0.87, 'gain': 0.3162, 'gainhf': 0.3981, 'gainlf': 0.5012,
        'decay_time': 1.12, 'decay_hfratio': 0.56, 'decay_lfratio': 0.18,
        'reflections_gain': 1.2589, 'reflections_delay': 0.01, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.4125, 'late_reverb_delay': 0.011, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.095, 'echo_depth': 0.14, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 7176.9, 'lfreference': 211.2,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Prefab Out House": {
        'density': 1.0, 'diffusion': 0.82, 'gain': 0.3162, 'gainhf': 0.1122, 'gainlf': 0.1585,
        'decay_time': 1.38, 'decay_hfratio': 0.38, 'decay_lfratio': 0.35,
        'reflections_gain': 0.8913, 'reflections_delay': 0.024, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.631, 'late_reverb_delay': 0.044, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.121, 'echo_depth': 0.17, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 2854.4, 'lfreference': 107.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Prefab Caravan": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.0891, 'gainlf': 0.1259,
        'decay_time': 0.43, 'decay_hfratio': 1.5, 'decay_lfratio': 1.0,
        'reflections_gain': 1.0, 'reflections_delay': 0.012, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.9953, 'late_reverb_delay': 0.012, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },

    # Dome and Pipe Presets
    "Dome Tomb": {
        'density': 1.0, 'diffusion': 0.79, 'gain': 0.3162, 'gainhf': 0.3548, 'gainlf': 0.2239,
        'decay_time': 4.18, 'decay_hfratio': 0.21, 'decay_lfratio': 0.1,
        'reflections_gain': 0.3868, 'reflections_delay': 0.03, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.6788, 'late_reverb_delay': 0.022, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.177, 'echo_depth': 0.19, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 2854.4, 'lfreference': 20.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Pipe Small": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.3548, 'gainlf': 0.2239,
        'decay_time': 5.04, 'decay_hfratio': 0.1, 'decay_lfratio': 0.1,
        'reflections_gain': 0.5012, 'reflections_delay': 0.032, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 2.5119, 'late_reverb_delay': 0.015, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 2854.4, 'lfreference': 20.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Dome Saint Pauls": {
        'density': 1.0, 'diffusion': 0.87, 'gain': 0.3162, 'gainhf': 0.3548, 'gainlf': 0.2239,
        'decay_time': 10.48, 'decay_hfratio': 0.19, 'decay_lfratio': 0.1,
        'reflections_gain': 0.1778, 'reflections_delay': 0.09, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.2589, 'late_reverb_delay': 0.042, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.12, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 2854.4, 'lfreference': 20.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Pipe Long Thin": {
        'density': 0.256, 'diffusion': 0.91, 'gain': 0.3162, 'gainhf': 0.4467, 'gainlf': 0.2818,
        'decay_time': 9.21, 'decay_hfratio': 0.18, 'decay_lfratio': 0.1,
        'reflections_gain': 0.7079, 'reflections_delay': 0.01, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.7079, 'late_reverb_delay': 0.022, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 2854.4, 'lfreference': 20.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Pipe Large": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.3548, 'gainlf': 0.2239,
        'decay_time': 8.45, 'decay_hfratio': 0.1, 'decay_lfratio': 0.1,
        'reflections_gain': 0.3981, 'reflections_delay': 0.046, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.5849, 'late_reverb_delay': 0.032, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 2854.4, 'lfreference': 20.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Pipe Resonant": {
        'density': 0.1373, 'diffusion': 0.91, 'gain': 0.3162, 'gainhf': 0.4467, 'gainlf': 0.2818,
        'decay_time': 6.81, 'decay_hfratio': 0.18, 'decay_lfratio': 0.1,
        'reflections_gain': 0.7079, 'reflections_delay': 0.01, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.0, 'late_reverb_delay': 0.022, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 2854.4, 'lfreference': 20.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },

    # Outdoors Presets
    "Outdoors Backyard": {
        'density': 1.0, 'diffusion': 0.45, 'gain': 0.3162, 'gainhf': 0.2512, 'gainlf': 0.5012,
        'decay_time': 1.12, 'decay_hfratio': 0.34, 'decay_lfratio': 0.46,
        'reflections_gain': 0.4467, 'reflections_delay': 0.069, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.7079, 'late_reverb_delay': 0.023, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.218, 'echo_depth': 0.34, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 4399.1, 'lfreference': 242.9,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Outdoors Rolling Plains": {
        'density': 1.0, 'diffusion': 0.0, 'gain': 0.3162, 'gainhf': 0.0112, 'gainlf': 0.631,
        'decay_time': 2.13, 'decay_hfratio': 0.21, 'decay_lfratio': 0.46,
        'reflections_gain': 0.1778, 'reflections_delay': 0.3, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.4467, 'late_reverb_delay': 0.019, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 1.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 4399.1, 'lfreference': 242.9,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Outdoors Deep Canyon": {
        'density': 1.0, 'diffusion': 0.74, 'gain': 0.3162, 'gainhf': 0.1778, 'gainlf': 0.631,
        'decay_time': 3.89, 'decay_hfratio': 0.21, 'decay_lfratio': 0.46,
        'reflections_gain': 0.3162, 'reflections_delay': 0.223, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.3548, 'late_reverb_delay': 0.019, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 1.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 4399.1, 'lfreference': 242.9,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Outdoors Creek": {
        'density': 1.0, 'diffusion': 0.35, 'gain': 0.3162, 'gainhf': 0.1778, 'gainlf': 0.5012,
        'decay_time': 2.13, 'decay_hfratio': 0.21, 'decay_lfratio': 0.46,
        'reflections_gain': 0.3981, 'reflections_delay': 0.115, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.1995, 'late_reverb_delay': 0.031, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.218, 'echo_depth': 0.34, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 4399.1, 'lfreference': 242.9,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Outdoors Valley": {
        'density': 1.0, 'diffusion': 0.28, 'gain': 0.3162, 'gainhf': 0.0282, 'gainlf': 0.1585,
        'decay_time': 2.88, 'decay_hfratio': 0.26, 'decay_lfratio': 0.35,
        'reflections_gain': 0.1413, 'reflections_delay': 0.263, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.3981, 'late_reverb_delay': 0.1, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.34, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 2854.4, 'lfreference': 107.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },

    # Mood Presets
    "Mood Heaven": {
        'density': 1.0, 'diffusion': 0.94, 'gain': 0.3162, 'gainhf': 0.7943, 'gainlf': 0.4467,
        'decay_time': 5.04, 'decay_hfratio': 1.12, 'decay_lfratio': 0.56,
        'reflections_gain': 0.2427, 'reflections_delay': 0.02, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.2589, 'late_reverb_delay': 0.029, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.08, 'modulation_time': 2.742, 'modulation_depth': 0.05,
        'air_absorption_gainhf': 0.9977, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Mood Hell": {
        'density': 1.0, 'diffusion': 0.57, 'gain': 0.3162, 'gainhf': 0.3548, 'gainlf': 0.4467,
        'decay_time': 3.57, 'decay_hfratio': 0.49, 'decay_lfratio': 2.0,
        'reflections_gain': 0.0, 'reflections_delay': 0.02, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.4125, 'late_reverb_delay': 0.03, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.11, 'echo_depth': 0.04, 'modulation_time': 2.109, 'modulation_depth': 0.52,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 139.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Mood Memory": {
        'density': 1.0, 'diffusion': 0.85, 'gain': 0.3162, 'gainhf': 0.631, 'gainlf': 0.3548,
        'decay_time': 4.06, 'decay_hfratio': 0.82, 'decay_lfratio': 0.56,
        'reflections_gain': 0.0398, 'reflections_delay': 0.0, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.122, 'late_reverb_delay': 0.0, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.474, 'modulation_depth': 0.45,
        'air_absorption_gainhf': 0.9886, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },

    # Driving Presets
    "Driving Commentator": {
        'density': 1.0, 'diffusion': 0.0, 'gain': 0.3162, 'gainhf': 0.5623, 'gainlf': 0.5012,
        'decay_time': 2.42, 'decay_hfratio': 0.88, 'decay_lfratio': 0.68,
        'reflections_gain': 0.1995, 'reflections_delay': 0.093, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.2512, 'late_reverb_delay': 0.017, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 1.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9886, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Driving Pit Garage": {
        'density': 0.4287, 'diffusion': 0.59, 'gain': 0.3162, 'gainhf': 0.7079, 'gainlf': 0.5623,
        'decay_time': 1.72, 'decay_hfratio': 0.93, 'decay_lfratio': 0.87,
        'reflections_gain': 0.5623, 'reflections_delay': 0.0, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.2589, 'late_reverb_delay': 0.016, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.11, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Driving In-Car Racer": {
        'density': 0.0832, 'diffusion': 0.8, 'gain': 0.3162, 'gainhf': 1.0, 'gainlf': 0.7943,
        'decay_time': 0.17, 'decay_hfratio': 2.0, 'decay_lfratio': 0.41,
        'reflections_gain': 1.7783, 'reflections_delay': 0.007, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.7079, 'late_reverb_delay': 0.015, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 10268.2, 'lfreference': 251.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Driving In-Car Sports": {
        'density': 0.0832, 'diffusion': 0.8, 'gain': 0.3162, 'gainhf': 0.631, 'gainlf': 1.0,
        'decay_time': 0.17, 'decay_hfratio': 0.75, 'decay_lfratio': 0.41,
        'reflections_gain': 1.0, 'reflections_delay': 0.01, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.5623, 'late_reverb_delay': 0.0, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 10268.2, 'lfreference': 251.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Driving In-Car Luxury": {
        'density': 0.256, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.1, 'gainlf': 0.5012,
        'decay_time': 0.13, 'decay_hfratio': 0.41, 'decay_lfratio': 0.46,
        'reflections_gain': 0.7943, 'reflections_delay': 0.01, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.5849, 'late_reverb_delay': 0.01, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 10268.2, 'lfreference': 251.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Driving Full Grandstand": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 0.2818, 'gainlf': 0.631,
        'decay_time': 3.01, 'decay_hfratio': 1.37, 'decay_lfratio': 1.28,
        'reflections_gain': 0.3548, 'reflections_delay': 0.09, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.1778, 'late_reverb_delay': 0.049, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 10420.2, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Driving Empty Grandstand": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.3162, 'gainhf': 1.0, 'gainlf': 0.7943,
        'decay_time': 4.62, 'decay_hfratio': 1.75, 'decay_lfratio': 1.4,
        'reflections_gain': 0.2082, 'reflections_delay': 0.09, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.2512, 'late_reverb_delay': 0.049, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 10420.2, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Driving Tunnel": {
        'density': 1.0, 'diffusion': 0.81, 'gain': 0.3162, 'gainhf': 0.3981, 'gainlf': 0.8913,
        'decay_time': 3.42, 'decay_hfratio': 0.94, 'decay_lfratio': 1.31,
        'reflections_gain': 0.7079, 'reflections_delay': 0.051, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.7079, 'late_reverb_delay': 0.047, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.214, 'echo_depth': 0.05, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 155.3,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },

    # City Presets
    "City Streets": {
        'density': 1.0, 'diffusion': 0.78, 'gain': 0.3162, 'gainhf': 0.7079, 'gainlf': 0.8913,
        'decay_time': 1.79, 'decay_hfratio': 1.12, 'decay_lfratio': 0.91,
        'reflections_gain': 0.2818, 'reflections_delay': 0.046, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.1995, 'late_reverb_delay': 0.028, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.2, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "City Subway": {
        'density': 1.0, 'diffusion': 0.74, 'gain': 0.3162, 'gainhf': 0.7079, 'gainlf': 0.8913,
        'decay_time': 3.01, 'decay_hfratio': 1.23, 'decay_lfratio': 0.91,
        'reflections_gain': 0.7079, 'reflections_delay': 0.046, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.2589, 'late_reverb_delay': 0.028, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.125, 'echo_depth': 0.21, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "City Museum": {
        'density': 1.0, 'diffusion': 0.82, 'gain': 0.3162, 'gainhf': 0.1778, 'gainlf': 0.1778,
        'decay_time': 3.28, 'decay_hfratio': 1.4, 'decay_lfratio': 0.57,
        'reflections_gain': 0.2512, 'reflections_delay': 0.039, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.8913, 'late_reverb_delay': 0.034, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.13, 'echo_depth': 0.17, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 2854.4, 'lfreference': 107.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "City Library": {
        'density': 1.0, 'diffusion': 0.82, 'gain': 0.3162, 'gainhf': 0.2818, 'gainlf': 0.0891,
        'decay_time': 2.76, 'decay_hfratio': 0.89, 'decay_lfratio': 0.41,
        'reflections_gain': 0.3548, 'reflections_delay': 0.029, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.8913, 'late_reverb_delay': 0.02, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.13, 'echo_depth': 0.17, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9943, 'hfreference': 2854.4, 'lfreference': 107.5,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "City Underpass": {
        'density': 1.0, 'diffusion': 0.82, 'gain': 0.3162, 'gainhf': 0.4467, 'gainlf': 0.8913,
        'decay_time': 3.57, 'decay_hfratio': 1.12, 'decay_lfratio': 0.91,
        'reflections_gain': 0.3981, 'reflections_delay': 0.059, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.8913, 'late_reverb_delay': 0.037, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.14, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.992, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "City Abandoned": {
        'density': 1.0, 'diffusion': 0.69, 'gain': 0.3162, 'gainhf': 0.7943, 'gainlf': 0.8913,
        'decay_time': 3.28, 'decay_hfratio': 1.17, 'decay_lfratio': 0.91,
        'reflections_gain': 0.4467, 'reflections_delay': 0.044, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.2818, 'late_reverb_delay': 0.024, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.2, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9966, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },

    # Misc. Presets
    "Dusty Room": {
        'density': 0.3645, 'diffusion': 0.56, 'gain': 0.3162, 'gainhf': 0.7943, 'gainlf': 0.7079,
        'decay_time': 1.79, 'decay_hfratio': 0.38, 'decay_lfratio': 0.21,
        'reflections_gain': 0.5012, 'reflections_delay': 0.002, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.2589, 'late_reverb_delay': 0.006, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.202, 'echo_depth': 0.05, 'modulation_time': 0.25, 'modulation_depth': 0.0,
        'air_absorption_gainhf': 0.9886, 'hfreference': 13046.0, 'lfreference': 163.3,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Chapel": {
        'density': 1.0, 'diffusion': 0.84, 'gain': 0.3162, 'gainhf': 0.5623, 'gainlf': 1.0,
        'decay_time': 4.62, 'decay_hfratio': 0.64, 'decay_lfratio': 1.23,
        'reflections_gain': 0.4467, 'reflections_delay': 0.032, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 0.7943, 'late_reverb_delay': 0.049, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.25, 'echo_depth': 0.0, 'modulation_time': 0.25, 'modulation_depth': 0.11,
        'air_absorption_gainhf': 0.9943, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Small Water Room": {
        'density': 1.0, 'diffusion': 0.7, 'gain': 0.3162, 'gainhf': 0.4477, 'gainlf': 1.0,
        'decay_time': 1.51, 'decay_hfratio': 1.25, 'decay_lfratio': 1.14,
        'reflections_gain': 0.8913, 'reflections_delay': 0.02, 'reflections_pan': (0.0, 0.0, 0.0),
        'late_reverb_gain': 1.4125, 'late_reverb_delay': 0.03, 'late_reverb_pan': (0.0, 0.0, 0.0),
        'echo_time': 0.179, 'echo_depth': 0.15, 'modulation_time': 0.895, 'modulation_depth': 0.19,
        'air_absorption_gainhf': 0.992, 'hfreference': 5000.0, 'lfreference': 250.0,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
}
