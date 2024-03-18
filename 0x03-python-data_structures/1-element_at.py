#!/usr/bin/python3

def element_at(my_list, idx):
    if idx >= 0 or idx < len(my_list):
        print("{}".format(my_list[idx]))
    elif idx < 0:
        print(None)
    elif idx >= len(my_list):
        print(None)
