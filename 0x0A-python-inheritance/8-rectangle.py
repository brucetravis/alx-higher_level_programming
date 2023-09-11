#!/usr/bin/python3


"""
This module defines the Rectangle class, which inherits from BaseGeometry.
"""


class BaseGeometry:
    """
    The BaseGeometry class contains methods for geometry-related operations.
    """

    def area(self):
        """
        Calculate the area (not implemented).

        Raises:
            Exception: This method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    The Rectangle class inherits from BaseGeometry and represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()  # Call the parent class constructor to set up validation
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(
            r._Rectangle__width, r._Rectangle__height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
