#!/usr/bin/python3
"""function that returns an object (Python data structure)
represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    Deserialize a JSON string to a Python data structure.

    Args:
        my_str (str): The JSON string to deserialize.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
