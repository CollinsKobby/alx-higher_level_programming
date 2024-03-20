#!/usr/bin/python3
def uniq_add(my_list=[]):
    nlist = list(set(my_list))
    sumd = 0
    for i in range(0, len(nlist)):
        sumd += nlist[i]
    return sumd
