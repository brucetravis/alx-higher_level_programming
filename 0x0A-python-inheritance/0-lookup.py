#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object for which to retrieve attributes and methods.

    Returns:
        list: A list of strings representing the attributes and methods.
    """
    return dir(obj)
