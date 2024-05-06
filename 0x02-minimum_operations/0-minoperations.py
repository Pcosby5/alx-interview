#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations

    Gets the fewest number of operations needed to
    result in exactly n 'H' characters.

    Algorithm:

    Starting with root = 2, find the smallest root such
    that n is evenly divisible by root.
    For each such root, the number of even divisions by
    root is the total number of operations
    needed to reach n.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The fewest number of operations needed to reach n 'H' characters.

    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if n < 2:
        return 0
    ops, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            # total even-divisions by root = total operations
            ops += root
            # set n to the remainder
            n = n // root
            # reduce root to find remaining smaller vals that evenly-divide n
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return ops
