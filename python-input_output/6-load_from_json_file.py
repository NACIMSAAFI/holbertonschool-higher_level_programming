#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""

import json


def load_from_json_file(filename):
    """
    Load JSON data from a file and return the corresponding
    Python data structure.

    Args:
        filename (str): The name of the JSON file to load from.

    Returns:
        object: The Python data structure represented by the JSON data.
    """
    with open(filename, "r") as f:
        return json.load(f)
