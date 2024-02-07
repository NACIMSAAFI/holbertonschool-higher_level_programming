#!/usr/bin/python3

"""
This script defines a Rectangle class with methods to calculate its area and
perimeter, and enforces the width and height attributes to be positive int.
"""


class Rectangle:

    """
    Constructor for the Rectangle class, initializing a rectangle with the
    given width and height values. Defaults to zero if no values are provided.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle object with the specified width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height

    """
    Method to calculate the area of the rectangle.

    Returns:
        int: The area of the rectangle.
    """

    def area(self):
        return self.width * self.height

    """
    Method to calculate the perimeter of the rectangle.

    Returns:
        int: The perimeter of the rectangle.
    """

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    """
    Returns a string representation of the rectangle, with '#' characters
    forming the outline of the rectangle.

    Returns:
        str: A string representing the rectangle.
    """

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.rstrip("\n")

    """
    Returns a string representation of the rectangle that can be used to
    recreate the object using eval().

    Returns:
        str: A string representation of the rectangle.
    """

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    """
    Destructor for the Rectangle class, prints a message when the object is
    deleted.
    """

    def __del__(self):
        print("Bye rectangle...")
