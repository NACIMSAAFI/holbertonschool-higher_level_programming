#!/usr/bin/python3
"""class will be the “base” of all other classes in this project. """


class Base:
    """
    Represents a base class with a private class attribute __nb_objects
    and an instance attribute id.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int, optional): The ID of the instance. If None,
            automatically assigns a unique ID.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
