#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.

    Args:
        filename (str): The name of the text file to be read.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
