#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 > 5:
    k = number % 10
    print("Last digit of {} is {} and is greater than 5".format(number, k))
elif number % 10 == 0:
    m = number % 10
    print("Last digit of {} is {} and is 0".format(number, m))
elif 0 < (number % 10) > 6:
    n = number % 10
    print(f"Last digit of {number:d} is {n:d} and is less than 6 and not 0")
