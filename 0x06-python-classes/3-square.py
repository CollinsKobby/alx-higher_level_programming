#!/usr/bin/python3
"""Module Description
THis a module description od a class Square
"""


class Square:
    """Square Class Documentation
    This a description of the Square class with functions __int__
    and area and contains exceptions
    """
    def __init__(self, size=0):
        """__init__"""
        if (type(size) != int):
            print("size must be an integer")
        if (size < 0):
            print("size must bi >= 0")
        else:
            self.__size = size

    def area(self):
        """area"""
        return(self.__size * 2)
