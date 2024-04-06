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
        
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)
