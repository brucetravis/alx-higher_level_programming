#!/usr/bin/python3

"""
This module defines an empty class BaseGeometry.
"""


class BaseGeometry:
    """
    This is the BaseGeometry class.
    """


if __name__ == "__main__":
    bg = BaseGeometry()

    print(f"BaseGeometry object: {bg}")
    print(f"Attributes and methods of bg:")
    print(dir(bg))
    print("Attributes and methods of BaseGeometry:")
    print(dir(BaseGeometry))
