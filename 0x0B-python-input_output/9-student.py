#!/usr/bin/python3
""" A module description of a class called Student
"""


class Student:
    """ A class called student containing the first_name,
    last_name and age """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ A function called class__to_json that
        returns the dict of an object """
        return (self.__dict__)
