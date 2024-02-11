#!/usr/bin/python3
"""Function that appends a string at the end of a text file (UTF8)
and returns the number of characters added"""


def append_write(filename="", text=""):
    """
    Append a string to a text file (UTF-8) and return the string appended.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        str: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
