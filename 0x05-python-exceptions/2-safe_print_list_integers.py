#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    t = 0
    for i in range(1, x+1):
        try:
            print("{:d}".format(my_list[t]), end="")
        except Exception:
            pass
        else:
            t += 1
    print()
    return (t)
