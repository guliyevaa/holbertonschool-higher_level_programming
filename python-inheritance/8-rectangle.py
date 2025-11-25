#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class"""


    def __init__(self, width, height):
        # Validate width and height using BaseGeometry method
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        # Assign private attributes
        self.__width = width
        self.__height = height
