#!/usr/bin/python3
""" A module of a function write_file """


def write_file(filename="", text=""):
    """ A function write_file that writes to a
    file """
    with open(filename, mode='w', encoding='utf-8') as myfile:
        return (myfile.write(text))
