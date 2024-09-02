#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Parameters:
    n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1  # Base case: the factorial of 0 is 1.
    else:
        return n * factorial(n-1)  # Recursive case: n * factorial of (n-1).

# Convert the first command-line argument to an integer and compute its factorial.
f = factorial(int(sys.argv[1]))

# Print the calculated factorial.
print(f)
