#!/usr/bin/python3
"""Lockboxes: DFS"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened
    First box is unlocked
    """
    if not boxes:
        return False

    opened_boxes = set([0])

    bx_in_stack = [0]
    while bx_in_stack:
        bx = bx_in_stack.pop()
        for key in boxes[bx]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                bx_in_stack.append(key)
    return len(opened_boxes) == len(boxes)
