#!/usr/bin/python3
"""
This module provides a function to write text to a UTF-8 file.
"""


def write_file(filename="", text=""):
    """UTF-8 text file and returns the number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
