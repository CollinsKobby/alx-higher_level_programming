#!/usr/bin/python3
""" This module takes the first and last name of an individual
"""


def say_my_name(first_name, last_name=""):
    """ say_my_nameprovides the first and last name of an individual
    Args:
    first_name - first name of the indivdual
    last_name - lasy name of an individual, set to "" by default
    return ("My name is <first name> <last name>") """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
