"""
Testing battery for angles.py
"""

import math

# import pytest
from angle_wrapper.angle_wrapper import wrap_to_pi, wrap_to_2pi, wrap_to_180, wrap_to_360


def test_wrap_to_pi():
    """
    Test wrap_to_pi function
    """
    radians = 3 * math.pi / 2
    assert wrap_to_pi(radians) == -math.pi / 2


def test_wrap_to_2pi():
    """
    Test wrap_to_2pi function
    """
    radians = 5 * math.pi / 2
    assert wrap_to_2pi(radians) == math.pi / 2


def test_wrap_to_180():
    """
    Test wrap_to_180 function
    """
    degrees = 270.0
    assert wrap_to_180(degrees) == -90.0


def test_wrap_to_360():
    """
    Test wrap_to_360 function
    """
    degrees = 450.0
    assert wrap_to_360(degrees) == 90.0
