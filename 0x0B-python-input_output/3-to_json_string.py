#!/usr/bin/python3
import json
""" A module of a function called to_json_string """


def to_json_string(my_obj):
    """ A function called to_json_string that the JSON
    representation of an object(string) """
    return json.dumps(my_obj)
