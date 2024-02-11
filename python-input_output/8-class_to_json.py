#!/usr/bin/python3
"""Function that returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object"""


def class_to_json(obj):
    """
    Serialize an instance of a Class into a JSON compatible dictionary.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary containing serializable attributes of the object.
    """
    attributes = obj.__dict__

    serializable_attributes = {}

    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_attributes[key] = value

    return serializable_attributes
