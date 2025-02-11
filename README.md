# Angle Wrapper

[![Python package](https://github.com/jbrodovsky/angle_wrapper/actions/workflows/python_project.yml/badge.svg)](https://github.com/jbrodovsky/angle_wrapper/actions/workflows/python_project.yml)

[![release](https://github.com/jbrodovsky/angle_wrapper/actions/workflows/python-publish.yml/badge.svg)](https://github.com/jbrodovsky/angle_wrapper/actions/workflows/python-publish.yml)

A simple Python only toolbox for wrapping angles to $\pm180^\circ$, $\left[0^\circ, 360^\circ\right]$, $\pm\pi$, or $\left[0,  2\pi\right]$. Wraps single values, tuples, lists, and other various iterable types that implement the `__iter__` attribute such as NumPy arrays and Pandas data series.

To install: `pip install anglewrapper`

To run:
```
from anglewrapper import wrap
wrap.to_180(270)
```

This package has no external dependancies to run in Python-only mode. Development and testing requires `pytest` or `unittest` installed in the local environment as well as numpy.
