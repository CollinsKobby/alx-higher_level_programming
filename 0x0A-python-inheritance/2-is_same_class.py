#!/usr/bin/python3
""" A module description of a simple function
is_same_class """


def is_same_class(obj, a_class):
    """ A function that checks if an object is an instance of
    a specified class. Returns True otherwisw return False when
    not """
    if type(obj) == a_class:
        return True
    else:
        return False
