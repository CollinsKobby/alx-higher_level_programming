#!/usr/bin/python3
""" A module of a class called Base """
import json


class Base:
    """ Class called Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns a JSON string representaon of
        list_dictionaries """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writs the JSON representation to list_objs """
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), 'w', encoding='UTF-8') as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON representation """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes set """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(2, 2)
        elif cls is Square:
            new = Square(2)
        else:
            new = None
        new.update(**dictionary)
        return new
