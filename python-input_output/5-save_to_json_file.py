#!/usr/bin/python3
"""Function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write the JSON representation of an object to a file.

    Args:
        my_obj: The object to be serialized to JSON.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
