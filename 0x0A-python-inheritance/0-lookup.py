#!/usr/bin/env python3

"""
This module defines a function to look up and retrieve 
the list of available attributes and methods of an object.
"""

def lookup(obj):
    """
    This function takes an object as an argument and 
    returns a list of its available attributes and methods.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the 
        attributes and methods of the object.
    """
    return dir(obj)

class MyClass1(object):
    pass



class MyClass2(object):
    my_attr1 = 3

    def my_meth(self):
        pass


# Print the attributes and methods of MyClass1, MyClass2, and int
print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
