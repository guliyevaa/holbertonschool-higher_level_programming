#!/usr/bin/env python3
"""
task_00_basic_serialization.py
Basic module to serialize a Python dictionary to a JSON file
and deserialize a JSON file back to a Python dictionary.
"""

import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file to a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

serialize_and_save_to_file(data_to_serialize, 'data.json')
print("Data serialized and saved to 'data.json'.")

deserialized_data = load_and_deserialize('data.json')
print("Deserialized Data:")
print(deserialized_data)

Data serialized and saved to 'data.json'.
Deserialized Data:
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
