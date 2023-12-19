"""
Python only toolbox for wrapping angles to a given range.
"""

import math


def to_pi(angle):
    """
    Wraps the given angle(s) to +/- pi.

    Parameters
    ----------
    :param angle: The values to wrap.
    :type angle: int, float, list[int], list[float], iterable[int], iterable[float]

    Returns
    --------
    :return: The wrapped values
    :rtype: int, float, list[int], list[float], iterable[int], iterable[float]

    Raises
    -------
    :raise TypeError: If the input data type is unsupported.
    """
    if isinstance(angle, (int, float)):
        return (angle + math.pi) % (2 * math.pi) - math.pi
    if isinstance(angle, list):
        return [to_pi(a) for a in angle]
    if isinstance(angle, tuple):
        return tuple(to_pi(a) for a in angle)
    if hasattr(angle, "__iter__"):  # Check if it's an iterable (including numpy array)
        return [to_pi(a) for a in angle]
    raise TypeError("Unsupported data type for angle")


def to_2pi(angle):
    """
    Wraps the given angle(s) to 2 pi.

    Parameters
    ----------
    :param angle: The values to wrap.
    :type angle: int, float, list[int], list[float], iterable[int], iterable[float]

    Returns
    --------
    :return: The wrapped values
    :rtype: int, float, list[int], list[float], iterable[int], iterable[float]

    Raises
    -------
    :raise TypeError: If the input data type is unsupported.
    """
    if isinstance(angle, (int, float)):
        return angle % (2 * math.pi)
    if isinstance(angle, list):
        return [to_2pi(a) for a in angle]
    if isinstance(angle, tuple):
        return tuple(to_2pi(a) for a in angle)
    if hasattr(angle, "__iter__"):
        return [to_2pi(a) for a in angle]
    raise TypeError("Unsupported data type for angle")


def to_180(angle):
    """
    Wraps the given angle(s) to 180.

    Parameters
    ----------
    :param angle: The values to wrap.
    :type angle: int, float, list[int], list[float], iterable[int], iterable[float]

    Returns
    --------
    :return: The wrapped values
    :rtype: int, float, list[int], list[float], iterable[int], iterable[float]

    Raises
    -------
    :raise TypeError: If the input data type is unsupported.
    """
    if isinstance(angle, (int, float)):
        return (angle + 180) % 360 - 180
    if isinstance(angle, list):
        return [to_180(a) for a in angle]
    if isinstance(angle, tuple):
        return tuple(to_180(a) for a in angle)
    if hasattr(angle, "__iter__"):
        return [to_180(a) for a in angle]
    raise TypeError("Unsupported data type for angle")


def to_360(angle):
    """
    Wraps the given angle(s) to 360.

    Parameters
    ----------
    :param angle: The values to wrap.
    :type angle: int, float, list[int], list[float], iterable[int], iterable[float]

    Returns
    --------
    :return: The wrapped values
    :rtype: int, float, list[int], list[float], iterable[int], iterable[float]

    Raises
    -------
    :raise TypeError: If the input data type is unsupported.
    """
    if isinstance(angle, (int, float)):
        return angle % 360
    if isinstance(angle, list):
        return [to_360(a) for a in angle]
    if isinstance(angle, tuple):
        return tuple(to_360(a) for a in angle)
    if hasattr(angle, "__iter__"):
        return [to_360(a) for a in angle]
    raise TypeError("Unsupported data type for angle")
