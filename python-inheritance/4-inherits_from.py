#!/usr/bin/python3
"""Function returns True if obj inherits from a_class."""

def inherits_from(obj, a_class):
    """Check if obj is an instance of class that inherited from a_class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
