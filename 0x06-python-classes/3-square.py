#!/usr/bin/python3
"""Module Description
THis a module description od a class Square
"""

class Square:
    def __init__(self, size=0):
        if (type(size) != int):
            print("size must be an integer")
        if (size < 0):
            print("size must bi >= 0")
        else:
            self.__size = size

    def area(self):
        return(self.__size * 2)
