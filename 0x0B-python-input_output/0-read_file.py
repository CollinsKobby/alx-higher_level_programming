#!/usr/bin/python3
""" A module of a simple function """


def read_file(filename=""):
    """ A function read_file that reads files
    """
    with open(filename, encoding='utf-8') as myfile:
        print(myfile.read(), end="")
