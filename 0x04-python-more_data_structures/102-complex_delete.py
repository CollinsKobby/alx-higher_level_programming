#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_value = list(a_dictionary.keys())
    for v in del_value:
        if a_dictionary[v] == value:
            del a_dictionary[v]
    return a_dictionary
