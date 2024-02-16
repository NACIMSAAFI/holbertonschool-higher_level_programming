#!/usr/bin/python3
""" Module for Rectangle class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, inherits from rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
            y (int, optional): The y-coordinate of the square's position.
            id (int, optional): The ID of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute"""

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the Square attributes based on the arguments provided.

        Args:
            *args (tuple): Arbitrary arguments in the order id,
            width, height, x, y.
            **kwargs (dict): Arbitrary keyword arguments.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        """Public method that returns the dictionary
        representation of a Square"""

        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y,
        }
