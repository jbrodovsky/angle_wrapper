"""Setup file for wrapfast."""

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

__version__ = "0.2.2"

ext_modules = [
    Pybind11Extension(
        "anglewrapper.wrapfast",
        ["src/anglewrapper/wrapfast.cpp"],
        define_macros=[("VERSION_INFO", __version__)],
    ),
]

setup(
    name="anglewrapper.wrapfast",
    version=__version__,
    author="James Brodovsky",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.9",
)
