"""
tester for anglewrapper
"""
from anglewrapper import wrap
from anglewrapper import wrapfast

import numpy as np


def main():
    """
    This is a test function.
    """
    print("Hello World!")

    print(wrap.to_180([1000, 200, 300]))
    print(wrapfast.to_180(300))
    print(wrapfast.to_180([1000, 200, 300]))
    # print(wrapfast.to_180(np.array([400, 200, 300])))


if __name__ == "__main__":
    main()
