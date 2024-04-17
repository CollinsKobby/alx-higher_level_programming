#!/usr/bin/python3
""" A module description of a function called
load_from_json_file """
import json


def load_from_json_file(filename):
    """ A function called load_from_json_file that
    creates an object ffrom a "JSON file" """
    with open(filename) as myfile:
        return json.loads(myfile.read())
