#!/usr/bin/python3
"""
    This is the Square class with private size attribute,
    getter, setter, and area method.
    """


class Square:
    """
    This is the Square class with private size attribute,
    getter, setter, and area method.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance.

        Parameters:
        - size (int, optional): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size.

        Parameters:
        - value (int): The size to be set.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size**2
