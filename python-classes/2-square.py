#!/usr/bin/python3


class Square:
    """
    This is the Square class with a private size attribute.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance.

        Parameters:
        - size (int, optional): The size of the square (default is 0).
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
