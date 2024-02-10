#!/usr/bin/python3
"""function that returns True if the object
is an instance of, or if the object is an instance
of a class that inherited from, the specified class ;
otherwise False."""


def inherits_from(obj, a_class):
    """
    Checks if the given object is an instance of a subclass
    of the specified class.

    Parameters:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a subclass
        of the specified class; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
