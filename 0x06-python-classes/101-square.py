#!/usr/bin/python3

"""
This module defines a Square class that represents a square shape.
"""


class Square:
    """
    A class representing a square shape.

    Attributes:
        size (int): The size of the square's sides.
        position (tuple): The position of the square's top-left corner.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square's sides (default is 0).
            position (tuple, optional): The position of the square's top-left corner (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is not a tuple.
            ValueError: If size is less than 0 or position values are less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(v, int) and v >= 0 for v in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using '#' characters.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        """
        String representation of the Square instance.

        Returns:
            str: Formatted string representation.
        """
        result = ""
        if self.__size == 0:
            return result

        for _ in range(self.__position[1]):
            result += "\n"
        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"

        return result.rstrip("\n")


if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
