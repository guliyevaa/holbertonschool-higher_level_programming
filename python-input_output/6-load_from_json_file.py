#!/usr/bin/python3
import json
"""doc"""


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
