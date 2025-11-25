#!/usr/bin/python3
"""
This module defines the MyList class.
MyList inherits from the built-in list class and adds a method
that prints the list in a sorted manner.
"""


class MyList(list):
    """A class that inherits from list and prints a sorted version of the list."""

    def print_sorted(self):
        """Print the list sorted in ascending order without modifying the original list."""
        print(sorted(self))
