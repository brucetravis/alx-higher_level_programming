#!/usr/bin/python3


"""
This module defines an empty class BaseGeometry.
"""


class BaseGeometry:
    pass


if __name__ == "__main__":
    bg = BaseGeometry()

    print(bg)  # Output: <__main__.BaseGeometry object at 0x7f2050c69208>
    print(dir(bg))
    print(dir(BaseGeometry))
