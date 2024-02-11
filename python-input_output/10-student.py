#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """
    Represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the given attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve.
                If None, all attributes will be retrieved.

        Returns:
            dict: A dictionary containing the selected attributes
            of the student.
        """
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age,
            }
        else:
            my_dict = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    my_dict.update({att: self.__dict__[att]})
            return my_dict
