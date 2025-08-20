import time

def seconds_to_nanoseconds(seconds: float) -> int:
    """
    Converts a duration in seconds to an integer number of nanoseconds.

    Args:
        seconds (float): The duration in seconds.

    Returns:
        int: The equivalent duration in nanoseconds.
    """
    return int(seconds * 1_000_000_000)

def get_future_time(device_clock: int, delay_in_seconds: float) -> int:
    """
    Calculates a future time on the device's clock.

    This is a convenience function for scheduling sounds to play after a
    certain delay.

    Args:
        device_clock (int): The current device clock time in nanoseconds,
                            typically from `device.get_clock()['clock']`.
        delay_in_seconds (float): The delay from the current clock time
                                  in seconds.

    Returns:
        int: The target absolute clock time in nanoseconds.
    """
    return device_clock + seconds_to_nanoseconds(delay_in_seconds)
