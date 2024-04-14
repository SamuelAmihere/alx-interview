#!/usr/bin/python3
"""Pascal's Triangle
"""

def pascal_triangle(n):
    """Pascal's Triangle: Python implementation"""
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if n <= 0:
        return []
    pascal = []
    for i in range(n):
        row = [1]
        if pascal:
            last_row = pascal[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        pascal.append(row)
    return pascal
