# Angle Wrapper

A simple Python only toolbox for wrapping angles to $\pm180^\circ$, $\left[0^\circ, 360^\circ\right]$, $\pm\pi$, or $\left[0,  2\pi\right]$. Wraps single values, tuples, lists, and other various iterable types that implement the `__iter__` attribute such as NumPy arrays and Pandas data series.

To install: `pip install anglewrapper`

To run:
```
from anglewrapper import wrap
wrap.to_180(270)
```

This package has no external dependancies to run in Python-only mode. Development and testing requires `pytest` or `unittest` installed in the local environment as well as numpy.

This package is serving a few purposes:

* Writing good Python code
* Some basic "agile" workflow practice including
  * Short lived branches for specific features
  * Unit testing
  * Code formatting and linting
* Continuous integration and continuous delivery to PyPI via GitHub Actions
* Building, testing, and delivering Python packages
* Some basic C++ practice and packaging it into libraries and/or Python packages 