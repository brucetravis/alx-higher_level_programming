#!/usr/bin/python3
"""Defines a class Student."""


def class_to_json(obj):
    """
    Converts an instance of a class to a JSON-serializable dictionary.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing the serialized attributes of the object.
    """

    return obj.__dict__
