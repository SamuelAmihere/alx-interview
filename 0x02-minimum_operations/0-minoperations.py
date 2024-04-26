#!/usr/bin/python3
"""AI is creating summary for
a text file with a single character H
"""


def minOperations(n):
    """Perorming Minimum operations"""
    if type(n) is not int or type(n) is float:
        return 0
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return 0
