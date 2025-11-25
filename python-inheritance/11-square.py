#!/usr/bin/python3
"""Square class that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        # Validate size using Rectangle's integer_validator
        self.integer_validator("size", size)
        # Private attribute
        self.__size = size
        # Call Rectangle constructor with width = height = size
        super().__init__(size, size)

    def __str__(self):
        """Return  description [Square] width/height"""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
