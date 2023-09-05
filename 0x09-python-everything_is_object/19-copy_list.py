#!/usr/bin/python3

'''
Module: 19-copy_list

This module defines a function `copy_list(l)` that returns a copy of a list `l`. The input list can contain any type of objects.

Example usage:
    my_list = [1, 2, 3]
    new_list = copy_list(my_list)
    print(new_list)  # Output: [1, 2, 3]
'''

def copy_list(l):
    return l[:]
