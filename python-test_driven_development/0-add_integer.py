#!/usr/bin/python3
"""
    Adds two integers or floats.

    Parameters:
    - a (int or float): The first number.
    - b (int or float, optional): The second number. Defaults to 98.

    Returns:
    - int: The sum of a and b as an integer.
    """


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Parameters:
    - a (int or float): The first number.
    - b (int or float, optional): The second number. Defaults to 98.

    Returns:
    - int: The sum of a and b as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer or float')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer or float')
    return int(a) + int(b)
