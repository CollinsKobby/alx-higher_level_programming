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
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
