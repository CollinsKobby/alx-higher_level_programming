#!/usr/bin/python3
""" Module description
A function that tells the inheritance of a class
"""


def is_kind_of_class(obj, a_class):
    """ A function that rreturns True when obj is an instance
    of the class a_class otherwise Returns False
    """
    return isinstance(obj, a_class)
