#!/usr/bin/python3
"""Function that returns True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.

."""


def inherits_from(obj, a_class):
    """
    Checks if the given object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class.

    Parameters:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance
        of a class that inherited from the specified class;
        otherwise False.
    """
    if type(obj) == a_class:
        return False

    for cls in type(obj).__mro__:
        if cls == a_class:
            return True
    return False
