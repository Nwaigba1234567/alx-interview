#!/usr/bin/python3
"""This module define a single function canUnlockAll
The function finds if a group of Box can all be
opened by accessing the first box
"""


def canUnlockAll(boxes):
    """An algorithm that check if all box in boxescan be opened

    Arguments:
    =========
    boxes (list of list): each list represents a box

    Returns (boolean): True if all every box can be accessed
    """

    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
