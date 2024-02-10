#!/usr/bin/python3
"""
    Function that returns True if the object is exactly an instance
    of the specified class ; otherwise False.
    """


def is_same_class(obj, a_class):
    """
    Checks if the given object is exactly an instance
    of the specified class.

    Parameters:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance
        of the specified class, False otherwise.
    """
    return type(obj) is a_class
