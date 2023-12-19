"""
Testing battery for angles.py
"""

import math
import numpy as np
import pandas as pd

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

    This function tests the behavior of the wrap_to_2pi function by checking if the result of
    wrapping the given radians to the range [0, 2pi) is equal to the expected value.
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


def test_to_180_negative():
    """
    Test wrap_to_180 function with negative input

    This function tests the wrap_to_180 function by passing a degree value of -270.0
    and asserting that the result is 90.0.
    """
    degrees = -270.0
    assert to_180(degrees) == 90.0


def test_to_360_negative():
    """
    Test wrap_to_360 function with negative input

    This function tests the behavior of the wrap_to_360 function by passing a value of
    -450.0 degrees and asserting that the result is 270.0 degrees.
    """
    degrees = -450.0
    assert to_360(degrees) == 270.0


def test_to_pi_negative():
    """
    Test wrap_to_pi function with negative input

    This function tests the wrap_to_pi function by checking if the result of wrapping
    the given radians to the range [-pi, pi) is equal to the expected value.
    """
    radians = -3 * math.pi / 2
    assert to_pi(radians) == math.pi / 2


def test_to_2pi_negative():
    """
    Test wrap_to_2pi function with negative input

    This function tests the behavior of the wrap_to_2pi function by checking if the
    result of wrapping the given radians to the range [0, 2pi) is equal to the expected
    value.
    """
    radians = -5 * math.pi / 2
    assert to_2pi(radians) == 3 * math.pi / 2


def test_to_180_range():
    """
    Test the wrap.to_180 function with a range of values in an iterable container such
    as a list or numpy array.
    """

    degrees = [-270.0, -90.0, 90.0, 270.0]
    expected = [90.0, -90.0, 90.0, -90.0]
    result = to_180(degrees)
    assert result == expected


def test_to_360_range():
    """
    Test the wrap.to_360 function with a range of values in an iterable container such
    as a list or numpy array.
    """

    degrees = [-450.0, -90.0, 90.0, 450.0]
    expected = [270.0, 270.0, 90.0, 90.0]
    result = to_360(degrees)
    assert result == expected


def test_to_pi_range():
    """
    Test the wrap.to_pi function with a range of values in an iterable container such
    as a list or numpy array.
    """

    radians = [-3 * math.pi / 2, -math.pi / 2, math.pi / 2, 3 * math.pi / 2]
    expected = [math.pi / 2, -math.pi / 2, math.pi / 2, -math.pi / 2]
    result = to_pi(radians)
    assert result == expected


def test_to_2pi_range():
    """
    Test the wrap.to_2pi function with a range of values in an iterable container such
    as a list or numpy array.
    """

    radians = [-5 * math.pi / 2, -math.pi / 2, math.pi / 2, 5 * math.pi / 2]
    expected = [3 * math.pi / 2, 3 * math.pi / 2, math.pi / 2, math.pi / 2]
    result = to_2pi(radians)
    assert result == expected


def test_to_180_numpy():
    """
    Test the wrap.to_180 function with a range of values in an iterable container such
    as a list or numpy array.
    """
    degrees = np.array([-270.0, -90.0, 90.0, 270.0])
    expected = np.array([90.0, -90.0, 90.0, -90.0])
    result = to_180(degrees)
    assert np.allclose(result, expected)


def test_to_360_numpy():
    """
    Test the wrap.to_360 function with a range of values in an iterable container such
    as a list or numpy array.
    """
    degrees = np.array([-450.0, -90.0, 90.0, 450.0])
    expected = np.array([270.0, 270.0, 90.0, 90.0])
    result = to_360(degrees)
    assert np.allclose(result, expected)


def test_to_pi_numpy():
    """
    Test the wrap.to_pi function with a range of values in an iterable container such
    as a list or numpy array.
    """
    radians = np.array([-3 * math.pi / 2, -math.pi / 2, math.pi / 2, 3 * math.pi / 2])
    expected = np.array([math.pi / 2, -math.pi / 2, math.pi / 2, -math.pi / 2])
    result = to_pi(radians)
    assert np.allclose(result, expected)


def test_to_2pi_numpy():
    """
    Test the wrap.to_2pi function with a range of values in an iterable container such
    as a list or numpy array.
    """
    radians = np.array([-5 * math.pi / 2, -math.pi / 2, math.pi / 2, 5 * math.pi / 2])
    expected = np.array([3 * math.pi / 2, 3 * math.pi / 2, math.pi / 2, math.pi / 2])
    result = to_2pi(radians)
    assert np.allclose(result, expected)


def test_to_180_pandas():
    """
    Test the wrap.to_180 function with a range of values in an iterable container such
    as a list or numpy array.
    """

    degrees = pd.Series([-270.0, -90.0, 90.0, 270.0])
    expected = pd.Series([90.0, -90.0, 90.0, -90.0])
    result = to_180(degrees)
    assert np.allclose(result, expected)


def test_to_2pi_pandas():
    """
    Test the wrap.to_2pi function with a range of values in an iterable container such
    as a list or numpy array.
    """

    radians = pd.Series([-5 * math.pi / 2, -math.pi / 2, math.pi / 2, 5 * math.pi / 2])
    expected = pd.Series([3 * math.pi / 2, 3 * math.pi / 2, math.pi / 2, math.pi / 2])
    result = to_2pi(radians)
    assert np.allclose(result, expected)
