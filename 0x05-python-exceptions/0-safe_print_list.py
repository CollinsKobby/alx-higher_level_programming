#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in my_list:
        t = 1
        try:
            while (t <= x):
                print("{}".format(i), end="")
                t += 1
        except IndexError:
            print("Index out of bounds")
    return(x)
