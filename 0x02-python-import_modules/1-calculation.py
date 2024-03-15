#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
"""if __name__ == "__main__":
    import sys
    add(sys.argv[0], sys.argv[0])
    sub(sys.argv[0], sys.argv[0])
    mul(sys.argv[0], sys.argv[0])
    div(int(sys.argv[0]), int(sys.argv[0]))
    """

a = 10
b = 5

print("{} + {} =".format(a, b), add(a, b))
print("{} - {} =".format(a, b), sub(a, b))
print("{} * {} =".format(a, b), mul(a, b))
print("{} / {} =".format(a, b), div(a, b))
