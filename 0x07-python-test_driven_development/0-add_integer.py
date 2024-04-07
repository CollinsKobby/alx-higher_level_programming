#!/usr/bin/python3
""" A function that adds two integers
Arguments:
    a - first number
    b- second number
 return a+b """


def add_integer(a, b=98):
    """ add_integer function documentation
    The function adds two integers a and b,
    if b is not given, b has been assigned to 98 and te value is used """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(a) is not float:
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        add = a + b
    return (add)
