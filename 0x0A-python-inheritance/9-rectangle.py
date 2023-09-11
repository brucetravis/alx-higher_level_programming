#!/usr/bin/python3

class BaseGeometry:
    """
    BaseGeometry class defines basic geometric operations.

    Attributes:
        None

    Methods:
        area(): Placeholder method to calculate the area of a shape.
        integer_validator(name, value): Validates that 'value' is a positive integer.
    """
    def area(self):
        """Placeholder method to calculate the area of a shape."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """
    Rectangle class represents a rectangle and inherits from BaseGeometry.

    Attributes:
        None

    Methods:
        __init__(self, width, height): Initializes a 
        Rectangle instance with width and height.
        area(): Calculates and returns the area of the rectangle.
        __str__(): Returns a string representation of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)        # Output: [Rectangle] 3/5
    print(r.area())  # Output: 15
