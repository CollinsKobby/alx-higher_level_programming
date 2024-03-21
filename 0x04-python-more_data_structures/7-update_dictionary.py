#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    upd = list(a_dictionary.keys())
    for i in upd:
        if i == key:
            a_dictionary[key] = value
        else:
            a_dictionary[key] = value

    return a_dictionary
