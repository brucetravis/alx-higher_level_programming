#!/usr/bin/python3

"""
This module defines a Rectangle class.

The Rectangle class has width and height attributes, as well as methods for calculating area and perimeter.
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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

if __name__ == "__main__":
    myrectangle = Rectangle(2, 4)
    print("{} - {} => {}".format(
        myrectangle.width, myrectangle.height, myrectangle.area()
    ))

    myrectangle = Rectangle(2, 4)
    print("{} - {} => {}".format(
        myrectangle.width, myrectangle.height, myrectangle.perimeter()
    ))

    myrectangle = Rectangle(10, 10)
    print("{} - {} => {} / {}".format(
        myrectangle.width, myrectangle.height, myrectangle.area(), myrectangle.perimeter()
    ))

    myrectangle = Rectangle(10)
    print("{} - {} => {} / {}".format(
        myrectangle.width, myrectangle.height, myrectangle.area(), myrectangle.perimeter()
    ))

    myrectangle = Rectangle()
    print("{} - {} => {} / {}".format(
        myrectangle.width, myrectangle.height, myrectangle.area(), myrectangle.perimeter()
    ))
