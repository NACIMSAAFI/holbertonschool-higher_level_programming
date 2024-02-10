#!/usr/bin/python3
"""
File: 1-my_list.py
Description: Defines a custom list class MyList
that inherits from the built-in list class.
             Provides a method print_sorted() to print
             the elements of the list in sorted order.
"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
