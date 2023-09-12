#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.

    Args:
        filename (str): The name of the text file to be read.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
