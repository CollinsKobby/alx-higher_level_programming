#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    del_keys = list(a_dictionary.keys())

    for i in del_keys:
        if i == key:
            del a_dictionary[i]
    return a_dictionary
