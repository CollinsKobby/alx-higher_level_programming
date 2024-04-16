#!/usr/bin/python3
""" Module Documentation
A module of a simple class lookup
"""


def lookup(obj):
    """ A simple function lookup which returns a list of
    attributes and methods of an object
    """
    return dir(obj)
