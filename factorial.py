#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        print("Current n:", n)
        result *= n
        n = n - 1
    return result

try:
    f = factorial(int(sys.argv[1]))
    print(f)
except KeyboardInterrupt:
    print("Program interrupted by user")
