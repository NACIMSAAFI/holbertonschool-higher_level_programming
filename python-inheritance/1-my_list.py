#!/usr/bin/python3
"""
Class MyList that inherits from list.
"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
