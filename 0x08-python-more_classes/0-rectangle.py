#!/usr/bin/python3

class Rectangle:
    """
    This is a simple Rectangle class.

    It can be used to represent rectangles with width and height attributes.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    pass


if __name__ == "__main__":
    # Example usage:
    my_rectangle = Rectangle()
    print(type(my_rectangle))
    print(my_rectangle.__dict__)
