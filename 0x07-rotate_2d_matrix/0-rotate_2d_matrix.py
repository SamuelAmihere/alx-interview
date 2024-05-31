#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate 2D Matrix
    """
    n = len(matrix)
    layers = n // 2
    # Loop through each layer
    for layer in range(layers):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # Save top
            top = matrix[layer][i]

            # Left -> Top
            matrix[layer][i] = matrix[-i - 1][layer]

            # Bottom -> Left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # Right -> Bottom
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

            # Top -> Right
            matrix[i][-layer - 1] = top
