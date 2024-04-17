#!/usr/bin/python3
""" A module of a function called append_write """


def append_write(filename="", text=""):
    """ A function append_write is a function that apeends text
    to an already existing file called filename """
    with open(filename, mode='a', encoding='utf-8') as myfile:
        return myfile.write(text)
