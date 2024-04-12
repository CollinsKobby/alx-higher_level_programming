#!/usr/bin/python3
"""This module prints # n times on n lines
"""


def print_square(size):
    """ The print_square function prints a square of size
    Args:
    size - size length of the square
    print_square(2)
    ##
    ## """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(0, size):
            print('#' * size)
            i += 1
