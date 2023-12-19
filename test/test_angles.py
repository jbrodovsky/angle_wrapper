"""
Testing battery for angles.py
"""

import math

# import pytest
from src.anglewrapper.wrap import to_pi, to_2pi, to_180, to_360


def test_to_pi():
    """
    Test wrap_to_pi function

    This function tests the wrap_to_pi function by checking if the result of wrapping
    the given radians to the range [-pi, pi) is equal to the expected value.
    """
    radians = 3 * math.pi / 2
    assert to_pi(radians) == -math.pi / 2


def test_to_2pi():
    """
    Test wrap_to_2pi function

    This function tests the behavior of the wrap_to_2pi function by checking if the result of wrapping
    the given radians to the range [0, 2pi) is equal to the expected value.
    """
    radians = 5 * math.pi / 2
    assert to_2pi(radians) == math.pi / 2


def test_to_180():
    """
    Test wrap_to_180 function

    This function tests the wrap_to_180 function by passing a degree value of 270.0
    and asserting that the result is -90.0.
    """
    degrees = 270.0
    assert to_180(degrees) == -90.0


def test_to_360():
    """
    Test wrap_to_360 function
    
    This function tests the behavior of the wrap_to_360 function by passing a value of 450.0 degrees
    and asserting that the result is 90.0 degrees.
    """
    degrees = 450.0
    assert to_360(degrees) == 90.0
