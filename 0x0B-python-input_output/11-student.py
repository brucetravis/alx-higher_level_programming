#!/usr/bin/python3


"""
This module defines a Student class with
serialization and deserialization methods.
"""


class Student:
    """
    Represents a student with attributes first_name, last_name, and age.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve (optional).

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(
                self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance 
        based on a provided dictionary.

        Args:
            json (dict): A dictionary with attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)

    def __str__(self):
        return "{} {} {}".format(self.first_name, self.last_name, self.age)
