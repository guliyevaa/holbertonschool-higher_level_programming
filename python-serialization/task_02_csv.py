#!/usr/bin/env python3
"""
task_02_csv.py
Convert CSV data into JSON format using serialization.
"""

import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON and save it as 'data.json'.

    Args:
        csv_filename (str): The path to the CSV file.

    Returns:
        bool: True if conversion succeeded, False otherwise.
    """
    try:
        # Read CSV data
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)  # Convert each row to dictionary

        # Write JSON data
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        return True

    except FileNotFoundError:
        # CSV file not found
        return False
    except Exception:
        # Any other exception
        return False
