#!/usr/bin/python3
"""Module Docuentation
This is a module description for a class Square
"""


class Square:
    """Square Class Documentation
    This a description of a class Square with instantiation size
    Raising some exceptions as well
    """

    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
