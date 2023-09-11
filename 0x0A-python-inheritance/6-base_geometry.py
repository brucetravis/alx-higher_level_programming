#!/usr/bin/python3


"""
This module defines a class BaseGeometry with an area() method.
"""


class BaseGeometry:
    def area(self):
        """
        Calculate the area (not implemented).

        Raises:
            Exception: This method is not implemented.
        """
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
