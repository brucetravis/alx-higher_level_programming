#!/usr/bin/python3


"""
This module defines a function that checks if an object is an 
instance of a class that 
inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that 
    inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class 
        that inherited from the specified class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class


# Usage example
if __name__ == "__main__":
    a = True

    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))


