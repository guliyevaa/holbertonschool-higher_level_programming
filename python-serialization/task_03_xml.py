#!/usr/bin/env python3
"""
task_03_xml.py
Serialize and deserialize Python dictionaries to and from XML format.
"""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename to save the XML data.
    """
    # Create root element
    root = ET.Element("data")

    # Add each key-value pair as a child element
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert value to string for XML

    # Write XML tree to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The XML file to read.

    Returns:
        dict: The deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        data = {}
        for child in root:
            data[child.tag] = child.text  # Keep as string
        return data
    except Exception:
        # Return empty dict if file not found or malformed
        return {}
