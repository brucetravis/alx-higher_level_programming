#!/usr/bin/python3

"""
This module defines the Rectangle class, which represents a geometric rectangle.

The Rectangle class includes attributes and methods for working with rectangles, such as calculating area and perimeter,
comparing rectangles, and more.

Attributes:
    number_of_instances (int): A class attribute to keep track of the number of Rectangle instances created.
    print_symbol (str): A class attribute used to specify the symbol for string representation of rectangles.

Methods:
    __init__(self, width=0, height=0): Initializes a Rectangle instance with the specified width and height.
    area(self): Calculates and returns the area of the rectangle.
    perimeter(self): Calculates and returns the perimeter of the rectangle.
    __str__(self): Returns a string representation of the rectangle using the specified print_symbol.
    __repr__(self): Returns a string representation of the Rectangle instance.
    __del__(self): Destructor method to clean up when a Rectangle instance is deleted.
    bigger_or_equal(rect_1, rect_2): Static method to compare two Rectangle instances and return the larger one.

"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) * self.__width
                          for _ in range(self.__height)])

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
