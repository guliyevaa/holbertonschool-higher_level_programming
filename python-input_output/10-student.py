#!/usr/bin/python3
"""
Class Student that defines a student (based on 9-student.py)
"""


class Student:
    """Defines a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary representation of the instance.
        If attrs is a list of strings, return only those attributes.
        Otherwise return all attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            result = {}
            for key in attrs:
                if hasattr(self, key):
                    result[key] = getattr(self, key)
            return result

        return self.__dict__
