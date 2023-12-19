"""
Python only toolbox for wrapping angles to a given range.
"""

import math


def to_pi(radians):
    """
    Wraps the given angle to the range [-pi, pi].
    """
    return (radians + math.pi) % (2 * math.pi) - math.pi


def to_2pi(radians):
    """
    Wraps the given angle to the range [0, 2pi].
    """
    return radians % (2 * math.pi)


def to_180(degrees):
    """
    Wraps the given angle to the range [-180, 180].
    """
    return (degrees + 180) % 360 - 180


def to_360(degrees):
    """
    Wraps the given angle to the range [0, 360].
    """
    return degrees % 360
