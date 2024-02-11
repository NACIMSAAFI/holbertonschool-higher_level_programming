#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """
    Convert the given object to a JSON formatted string.

    Args:
        my_obj: The object to be converted.

    Returns:
        str: The JSON formatted string representing the object.
    """
    return json.dumps(my_obj)
