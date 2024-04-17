#!/usr/bin/python3
""" A module description of a function called
class_to_join """
import json


def class_to_json(obj):
    """ A function called class__to_json that
    returns the dict of an object """
    return json.dumps(obj.__dict__)
