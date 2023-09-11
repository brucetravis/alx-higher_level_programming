#!/usr/bin/python3

"""
This module defines a function that checks if an object is an instance of, or if it inherits from, a specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or inherits from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of or inherits from the specified class, otherwise False.
    """
    return isinstance(obj, a_class)

# Usage example
if __name__ == "__main__":
    a = 1

    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
