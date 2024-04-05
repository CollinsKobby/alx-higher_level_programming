#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    for i in range(1, x+1):
        try:
            print("{}".format(my_list[number]), end="")
        except Exception as e:
            break
        else:
            number += 1
    print()
    return (number)
