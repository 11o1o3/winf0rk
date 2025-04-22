import time

timers = {}


def start_timer(name):
    """
    Starts a timer with the given name.
    :param name: The name of the timer.
    """
    timers[name] = time.time()


def stop_timer(name):
    """
    Stops a timer and returns the elapsed time in milliseconds.
    :param name: The name of the timer.
    :return: Elapsed time in milliseconds or None if timer does not exist.
    """
    if name in timers:
        elapsed_time = (time.time() - timers[name]) * 1000
        del timers[name]
        return int(elapsed_time)
    else:
        return None


def get_timer_state(name):
    """
    Retrieves the elapsed time of a running timer in milliseconds.
    :param name: The name of the timer.
    :return: Elapsed time in milliseconds or None if timer does not exist.
    """
    if name in timers:
        elapsed_time = (time.time() - timers[name]) * 1000
        return int(elapsed_time)
    else:
        return None