"""
This module contains predefined effect settings for the standard Reverb effect,
ported from the efx-presets.h header in the OpenAL Soft SDK.

The keys are user-friendly names that can be passed to the 
Reverb.apply_preset() method.
"""

# NOTE: The standard Reverb effect is a simplified version of EAX Reverb.
# These presets are derived from the EAX presets but map to the more limited
# standard Reverb parameters.

PRESETS = {
    "Default": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 1.49, 'decay_hfratio': 0.83, 'reflections_gain': 0.05,
        'reflections_delay': 0.007, 'late_reverb_gain': 1.26,
        'late_reverb_delay': 0.011, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Generic": { # Same as Default
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 1.49, 'decay_hfratio': 0.83, 'reflections_gain': 0.05,
        'reflections_delay': 0.007, 'late_reverb_gain': 1.26,
        'late_reverb_delay': 0.011, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Padded Cell": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 0.17, 'decay_hfratio': 0.1, 'reflections_gain': 0.2,
        'reflections_delay': 0.002, 'late_reverb_gain': 0.28,
        'late_reverb_delay': 0.003, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Room": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 0.4, 'decay_hfratio': 0.83, 'reflections_gain': 0.21,
        'reflections_delay': 0.003, 'late_reverb_gain': 0.4,
        'late_reverb_delay': 0.004, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Bathroom": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 1.49, 'decay_hfratio': 0.54, 'reflections_gain': 0.4,
        'reflections_delay': 0.007, 'late_reverb_gain': 0.9,
        'late_reverb_delay': 0.011, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Living Room": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 0.5, 'decay_hfratio': 0.1, 'reflections_gain': 0.13,
        'reflections_delay': 0.003, 'late_reverb_gain': 0.2,
        'late_reverb_delay': 0.004, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Stone Room": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 2.31, 'decay_hfratio': 0.64, 'reflections_gain': 0.3,
        'reflections_delay': 0.012, 'late_reverb_gain': 0.5,
        'late_reverb_delay': 0.017, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Auditorium": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 4.32, 'decay_hfratio': 0.59, 'reflections_gain': 0.1,
        'reflections_delay': 0.02, 'late_reverb_gain': 0.2,
        'late_reverb_delay': 0.03, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Concert Hall": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 3.92, 'decay_hfratio': 0.7, 'reflections_gain': 0.1,
        'reflections_delay': 0.02, 'late_reverb_gain': 0.26,
        'late_reverb_delay': 0.029, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Cave": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 2.91, 'decay_hfratio': 1.3, 'reflections_gain': 0.2,
        'reflections_delay': 0.015, 'late_reverb_gain': 0.44,
        'late_reverb_delay': 0.022, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Arena": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 7.24, 'decay_hfratio': 0.33, 'reflections_gain': 0.1,
        'reflections_delay': 0.02, 'late_reverb_gain': 0.26,
        'late_reverb_delay': 0.03, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Hangar": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 10.05, 'decay_hfratio': 0.23, 'reflections_gain': 0.2,
        'reflections_delay': 0.02, 'late_reverb_gain': 0.3,
        'late_reverb_delay': 0.03, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Carpeted Hallway": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.1,
        'decay_time': 0.3, 'decay_hfratio': 0.1, 'reflections_gain': 0.12,
        'reflections_delay': 0.002, 'late_reverb_gain': 0.15,
        'late_reverb_delay': 0.03, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Hallway": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 1.49, 'decay_hfratio': 0.59, 'reflections_gain': 0.25,
        'reflections_delay': 0.007, 'late_reverb_gain': 1.66,
        'late_reverb_delay': 0.011, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Stone Corridor": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 2.7, 'decay_hfratio': 0.79, 'reflections_gain': 0.25,
        'reflections_delay': 0.013, 'late_reverb_gain': 1.58,
        'late_reverb_delay': 0.02, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Alley": {
        'density': 1.0, 'diffusion': 0.3, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 1.49, 'decay_hfratio': 0.86, 'reflections_gain': 0.25,
        'reflections_delay': 0.007, 'late_reverb_gain': 1.0,
        'late_reverb_delay': 0.011, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Forest": {
        'density': 1.0, 'diffusion': 0.3, 'gain': 0.32, 'gainhf': 0.02,
        'decay_time': 1.49, 'decay_hfratio': 0.54, 'reflections_gain': 0.05,
        'reflections_delay': 0.162, 'late_reverb_gain': 0.77,
        'late_reverb_delay': 0.088, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "City": {
        'density': 1.0, 'diffusion': 0.5, 'gain': 0.32, 'gainhf': 0.4,
        'decay_time': 1.49, 'decay_hfratio': 0.67, 'reflections_gain': 0.07,
        'reflections_delay': 0.007, 'late_reverb_gain': 0.14,
        'late_reverb_delay': 0.011, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Mountains": {
        'density': 1.0, 'diffusion': 0.27, 'gain': 0.32, 'gainhf': 0.06,
        'decay_time': 1.49, 'decay_hfratio': 0.21, 'reflections_gain': 0.04,
        'reflections_delay': 0.3, 'late_reverb_gain': 0.19,
        'late_reverb_delay': 0.1, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Quarry": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.32,
        'decay_time': 1.49, 'decay_hfratio': 0.83, 'reflections_gain': 0.0,
        'reflections_delay': 0.061, 'late_reverb_gain': 1.78,
        'late_reverb_delay': 0.025, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Plain": {
        'density': 1.0, 'diffusion': 0.21, 'gain': 0.32, 'gainhf': 0.1,
        'decay_time': 1.49, 'decay_hfratio': 0.5, 'reflections_gain': 0.06,
        'reflections_delay': 0.179, 'late_reverb_gain': 0.11,
        'late_reverb_delay': 0.1, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Parking Lot": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 1.0,
        'decay_time': 1.65, 'decay_hfratio': 1.5, 'reflections_gain': 0.21,
        'reflections_delay': 0.008, 'late_reverb_gain': 0.27,
        'late_reverb_delay': 0.012, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': False
    },
    "Sewer Pipe": {
        'density': 1.0, 'diffusion': 0.8, 'gain': 0.32, 'gainhf': 0.14,
        'decay_time': 2.81, 'decay_hfratio': 0.14, 'reflections_gain': 0.4,
        'reflections_delay': 0.014, 'late_reverb_gain': 1.0,
        'late_reverb_delay': 0.021, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
    "Underwater": {
        'density': 1.0, 'diffusion': 1.0, 'gain': 0.32, 'gainhf': 0.89,
        'decay_time': 1.49, 'decay_hfratio': 0.1, 'reflections_gain': 0.07,
        'reflections_delay': 0.007, 'late_reverb_gain': 2.0,
        'late_reverb_delay': 0.011, 'air_absorption_gainhf': 0.994,
        'room_rolloff_factor': 0.0, 'decay_hflimit': True
    },
}
