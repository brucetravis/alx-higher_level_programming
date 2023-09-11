#!/usr/bin/python3

def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute should be added.
        attribute (str): The name of the attribute.
        value: The value to set for the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if hasattr(obj, "__dict__") or (hasattr(obj, "__slots__") and attribute in obj.__slots__):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
