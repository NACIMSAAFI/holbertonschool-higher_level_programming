#!/usr/bin/python3
"""
This script defines a Square class that inherits from Rectangle.
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.

    """

    def __init__(self, size):
        """
        Initializes a Square object with the given size.
        """
        super().__init__(size, size)
        self.__size = size
