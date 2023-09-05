#!/usr/bin/python3


'''
Module: 101-locked_class

This module defines a class `LockedClass` that restricts the creation of instance 
attributes to only 'first_name'. Any attempt to create other instance attributes will raise an AttributeError.

Example usage:
    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.last_name = "Snow"
    except AttributeError as e:
        print("[{}] {}".format(e.__class__.__name__, e))
'''
class LockedClass:
    __slots__ = ('first_name',)

