#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize the square with a positive integer size."""
        self.integer_validator("size", size)
        self._Rectangle__width = size
        self._Rectangle__height = size

    def area(self):
        """Return the area of the square."""
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """Return the square description [Square] width/height."""
        w = self._Rectangle__width
        h = self._Rectang_
