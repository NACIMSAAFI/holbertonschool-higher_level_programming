#!/usr/bin/python3
"""
Class MyList that inherits from list.
"""


class MyList(list):
    """
    Prints the elements of the list in sorted order.
    """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
