#!/usr/bin/python3
"""Module Documentation
A description of a class Square
"""


class Square:
    """ Class Square Documentation
    A decription of the class square with methods size and add
    """
    def __init__(self, size=0, position=(0, 0)):
        """__init__"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Print area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """ Print ###"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
