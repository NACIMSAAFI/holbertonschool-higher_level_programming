#!/usr/bin/python3
"""
Rectangle Class: Defines a rectangle object with specified width and height.

Attributes:
    width_value (int): The width of the rectangle.
    height_value (int): The height of the rectangle.

Methods:
    __init__(self, width=0, height=0): Initializes a Rectangle object
    with specified width and height.
"""


class Rectangle:
    """
    Initializes a Rectangle object with specified width and height.

    Args:
        width (int): The width of the rectangle (default is 0).
        height (int): The height of the rectangle (default is 0).

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than 0.
    """

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width_value = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height_value = height
