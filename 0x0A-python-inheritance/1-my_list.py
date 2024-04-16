#!/usr/bin/python3
""" Module Description
A module description of a class Called Mylist
"""


class MyList(list):
    def __init__(self):
        self

    @property
    def num(self):
        return self

    @num.setter
    def num(self, value):
        if not isinstance(value, int):
            raise TypeError("Value should be an integer")
        else:
            self = value

    def print_sorted(self):
        return sorted(self)
