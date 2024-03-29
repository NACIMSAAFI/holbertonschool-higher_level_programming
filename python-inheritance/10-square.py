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
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

        def area(self):
            """
            Calculates the area of the square.

            Returns:
                int: The area of the square.
            """
            return self.__size * self.__size
