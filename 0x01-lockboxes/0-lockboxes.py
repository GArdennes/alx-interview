#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """
    A function that determine if all the boxes are opened
    """
    accessible = [0]
    keys = set(accessible)

    for key in accessible:
        for new_key in boxes[key]:
            if 0 <= new_key < len(boxes) and new_key not in keys:
                accessible.append(new_key)
                keys.add(new_key)
    return len(boxes) == len(accessible)
