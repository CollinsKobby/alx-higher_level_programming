#!/usr/bin/python3

def search_replace(my_list, search, replace):
    n_list = my_list[:]
    for i in range(0, len(my_list)):
        if my_list[i] == search:
            n_list[i] = replace

    return n_list
