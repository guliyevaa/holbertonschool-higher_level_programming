#!/usr/bin/python3
"""
Script that adds all arguments to a Python list and saves them to a file.
"""

import sys
from os import path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

# If file exists → load the list
if path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add command line arguments (skip script name)
items.extend(sys.argv[1:])

# Save updated list to file
save_to_json_file(items, filename)
