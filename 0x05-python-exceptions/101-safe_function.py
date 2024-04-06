#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct(args[0], args[1])
    except Exception as ex:
        print("Exception: {}".format(ex), file=sys.stderr)
        return (None)
    else:
        return (fct())
