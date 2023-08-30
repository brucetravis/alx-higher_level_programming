#!/usr/bin/python3

class Square:
    """
    A class to represent a square.
    
    Attributes:
        __size (int): The size of the square.
    """
    
    def __init__(self, size=0):
        """
        Initialize a new Square instance.
        
        Args:
            size (int, optional): The size of the square (default is 0).
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.
        
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
