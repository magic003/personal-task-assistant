import time


def current_time() -> int:
    """Gets the user's current time in seconds since the epoch.

    Returns:
        int: Current time in seconds since the epoch.
    """
    return int(time.time())
