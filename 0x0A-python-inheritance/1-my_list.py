#!/usr/bin/python3
""" Module Description
A module description of a class Called Mylist
"""


class MyList(list):
    def print_sorted(self):
        self.sort()
        return self
