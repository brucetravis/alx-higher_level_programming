#!/usr/bin/python3

"""
This module defines a Rectangle class.

The Rectangle class has width and height attributes.
"""


class Rectangle:
    """
    This is a simple Rectangle class.

    It can be used to represent rectangles with width and height attributes.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


if __name__ == "__main__":
    # Example usage:
    myrectangle = Rectangle(2, 4)
    print(sorted(myrectangle.__dict__))

    try:
        myrectangle.width = -4
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        myrectangle.height = "4"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    print(myrectangle.width)
    print(myrectangle.height)

    myrectangle = Rectangle(4)
    print("{} - {}".format(myrectangle.width, myrectangle.height))

    myrectangle = Rectangle()
    print("{} - {}".format(myrectangle.width, myrectangle.height))

    myrectangle = Rectangle(2, 4)
    print("{} - {}".format(myrectangle.width, myrectangle.height))
    myrectangle.width = 10
    print("{} - {}".format(myrectangle.width, myrectangle.height))

    myrectangle = Rectangle(2, 4)
    print("{} - {}".format(myrectangle.width, myrectangle.height))
    myrectangle.height = 10
    print("{} - {}".format(myrectangle.width, myrectangle.height))

    try:
        myrectangle = Rectangle(2, "3")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        myrectangle = Rectangle("2", 3)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
