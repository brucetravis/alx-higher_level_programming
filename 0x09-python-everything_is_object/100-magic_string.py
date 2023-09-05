#!/usr/bin/python3

'''
Module: 100-magic_string

This module defines a function `magic_string()` that returns a string "BestSchool" repeated n times, where n is the number of times the function has been called.

Example usage:
    for i in range(10):
        print(magic_string())
'''

def magic_string():
    if not hasattr(magic_string, 'count'):
        magic_string.count = 0
    else:
        magic_string.count += 1
    return "BestSchool, " * magic_string.count + "BestSchool"
