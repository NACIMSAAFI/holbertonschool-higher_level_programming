#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string declaring the provided names.

    Parameters:
    - first_name (str): Required string representing the first name.
    - last_name (str, optional): Optional string representing the last name
      (default is an empty string).

    Raises:
    - TypeError: If first_name is not a string or if last_name (when provided)
      is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {}$".format(first_name + " " + last_name))
