#!/usr/bin/python3
"""
Function that returns the list of available attributes and methods
of an object
   """


def lookup(obj):
    """
    Provides a comprehensive list of attributes and methods
    associated with the given object.

    Parameters:
        obj (object): The object to inspect.

    Returns:
        list: A list containing the names of attributes and methods
        accessible on the object.
    """
    return dir(obj)
