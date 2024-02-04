#!/usr/bin/python3
"""
This is the Square class with private size and position attributes,
getters, setters, area method, and my_print method.
"""


class Square:
    """
    This is the Square class with private size and position attributes,
    getters, setters, area method, and my_print method.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square instance.

        Parameters:
        - size (int, optional): The size of the square (default is 0).
        - position (tuple, optional): The position of the square
        (default is (0, 0)).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method to retrieve the position.

        Returns:
        - tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position.

        Parameters:
        - value (tuple): The position to be set.

        Raises:
        - TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            type(value) is not tuple
            or len(value) != 2
            or not all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """
        Prints the square with the character '#'.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
