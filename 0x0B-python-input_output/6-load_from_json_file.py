#!/usr/bin/python3
"""Defines a JSON file-reading function."""


import json


def load_from_json_file(filename):
    """
    Loads an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object represented by the JSON data.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
