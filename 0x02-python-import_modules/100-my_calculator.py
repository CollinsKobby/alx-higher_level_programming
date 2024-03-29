#!/usr/bin/python3
import sys
from calculator_1.py import add, sub, mul, div
if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
if argv[2] not in ('+', '-', '*', '/'):
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])
if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    result = a / b
print("{} {} {} = {}".format(a, operator, b, result))
