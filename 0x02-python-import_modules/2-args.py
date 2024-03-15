#!/usr/bin/python3

from sys import argv

if len(argv) == 1:
    print("{} arguments.".format(len(argv) - 1))
elif len(argv) > 1:
    if len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
    elif len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))

"""if __name__ == "__main__":
    2-args()"""
