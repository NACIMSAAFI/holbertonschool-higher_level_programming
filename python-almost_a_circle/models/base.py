#!/usr/bin/python3
"""class will be the “base” of all other classes in this project. """


class Base:
    """
    Represents a base class with a private class attribute __nb_objects
    and an instance attribute id.
    """

    import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON-formatted string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON-formatted string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return Base.json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs])

        with open(filename, "w") as file:
            file.write(json_string)

    def from_json_string(json_string):
        """
        Deserializes a JSON-formatted string into Python objects.

        Args:
            json_string (str): JSON-formatted string.

        Returns:
            list: Python objects deserialized from the JSON string.
        """
        if json_string is None:
            return []
        else:
            return Base.json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already
        set based on a dictionary.

        Args:
            **dictionary: Double pointer to a dictionary
            containing attributes.

        Returns:
            Instance: An instance of the class with attributes
            set from the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class")

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a file and return a list of instances.

        Returns:
            list: A list of instances loaded from the file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                if not json_string:
                    return []
                dictionary_list = cls.from_json_string(json_string)
                instance_list = []
                for dictionary in dictionary_list:
                    instance = cls.create(**dictionary)
                    instance_list.append(instance)
                return instance_list
        except FileNotFoundError:
            return []
