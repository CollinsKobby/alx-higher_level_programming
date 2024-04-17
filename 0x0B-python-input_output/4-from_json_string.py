#!/usr/bin/python3
""" A module description of a function called
from_json_string """
import json


def from_json_string(my_str):
    """ A function from_json_string that returns an
    object represented by a JSON string """
    return json.loads(my_str)
