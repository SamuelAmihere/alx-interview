#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.

implementation:
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
"""
import sys


def get_input():
    """
    Get the input from the user
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    return n


def attacking(pos1, pos2):
    """
    Check if two queens are attacking each other
    """
    return pos1[0] == pos2[0] or\
        pos1[1] == pos2[1] or\
        abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def exists(group):
    """
    Check if a queen exists in the same row or column
    """
    for i in range(len(group) - 1):
        for j in range(i + 1, len(group)):
            if attacking(group[i], group[j]):
                return True
    return False


def solution(row, group):
    """
    Find the solution
    """
    if row == n:
        if not exists(group):
            print(group)
        return
    for i in range(n):
        group.append([row, i])
        if not exists(group):
            solution(row + 1, group)
        group.pop()


def solve():
    """
    Solve the n queens problem
    """
    solution(0, [])


if __name__ == "__main__":
    n = get_input()
    solve()
