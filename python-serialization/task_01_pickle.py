#!/usr/bin/env python3
"""
task_01_pickle.py
Serialize and deserialize custom Python objects using the pickle module.
"""

import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object instance to a file using pickle.
        
        Args:
            filename (str): The filename to save the serialized object.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            # Return None if serialization fails
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a file to return an instance of CustomObject.

        Args:
            filename (str): The filename to load the serialized object from.

        Returns:
            CustomObject or None: Returns the object if successful, otherwise None.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            # Return None if file doesn't exist or deserialization fails
            return None
