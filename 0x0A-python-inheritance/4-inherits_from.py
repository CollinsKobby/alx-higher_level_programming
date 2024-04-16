#!/usr/bin/python3
""" Module description
A simple function """


def inherits_from(obj, a_class):
    """ A function that returns True when obj is an instance of a
    class that inherited (directly or indirectly from a_class,
    otherwise False """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
