#!/usr/bin/python3
"""
This is the Square class.
"""


class Square:
    """
    This is the Square class with a private size attribute.

    Parameters:
    - size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes the Square instance.

        Parameters:
        - size (int): The size of the square.
        """

        self.__size = size
