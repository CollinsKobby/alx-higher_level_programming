#!/usr/bin/python3
"""Module Documentation
A description of a class Square
"""


class Square:
    """ Class Square Documentation
    A decription of the class square with methods size and add
    """
    def __init__(self, size=0):
        """__init__"""
        try:
            type(size) is int
            size >= 0
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must bi >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        return (self.__size ** 2)
