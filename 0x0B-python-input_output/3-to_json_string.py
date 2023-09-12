#!/usr/bin/python3
"""String to JSON serialization utility."""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object as a string.

    Args:
        my_obj: The object to be serialized to JSON.

    Returns:
        A JSON string representing the object.
    """
    return json.dumps(my_obj)
