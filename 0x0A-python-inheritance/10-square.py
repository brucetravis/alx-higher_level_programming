#!/usr/bin/python3
"""
Module for the Square class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.
    """
    def __init__(self, size):
        """
        Initialize a Square object.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is not a positive integer.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format [Square] size/size.
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
