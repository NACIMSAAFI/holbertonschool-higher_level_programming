#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
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

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 and self.height == 0:
            return 0
        return 2 * (self.width + self.height)
