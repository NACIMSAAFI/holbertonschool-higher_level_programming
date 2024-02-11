#!/usr/bin/python3
"""Function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename):
    """
    Read and print the content of the specified file.

    Args:
        filename (str): The path to the file to be read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        print(text)
