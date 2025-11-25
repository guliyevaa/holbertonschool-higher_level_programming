#!/usr/bin/python3
"""
This module defines the lookup function.
It returns a list of available attributes and methods of an object.
"""


def lookup(obj):
    """Return list of attributes and methods of an object."""
    return dir(obj)
