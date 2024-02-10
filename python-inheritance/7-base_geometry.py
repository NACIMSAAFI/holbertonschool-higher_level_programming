#!/usr/bin/python3
"""A class BaseGeometry"""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Calculate the area of the geometric shape."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method: def
        integer_validator(self, name, value): that validates value

        Parameters:
            name (str): The name .
            value (int): The parameter.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
