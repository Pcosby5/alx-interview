#!/usr/bin/python3
"""
This module provides a function to determine if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    UTF-8 encoding can be from 1 to 4 bytes long. The encoding rules are:
    - 1-byte character: 0xxxxxxx
    - 2-byte character: 110xxxxx 10xxxxxx
    - 3-byte character: 1110xxxx 10xxxxxx 10xxxxxx
    - 4-byte character: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

    Parameters:
    data (list of int): A list of integers representing the data set,
                        where each integer represents a byte (only the
                        8 least significant bits are considered).

    Returns:
    bool: True if the data set is a valid UTF-8 encoding, False otherwise.

    Examples:
    >>> validUTF8([65])
    True

    >>> validUTF8([80, 121, 116, 104, 111, 110, 32, 105, 115, 32,
                   99, 111, 111, 108, 33])
    True

    >>> validUTF8([229, 65, 127, 256])
    False

    The function works by iterating through each byte in the data set:
    - If num_bytes is 0, it determines the number of bytes the current
      UTF-8 character consists of by checking the leading bits.
    - If num_bytes is greater than 0, it checks that each subsequent byte
      starts with '10', indicating it is a continuation byte.
    - If any byte does not meet the expected pattern, the function returns
      False.
    - At the end, the function returns True only if all characters have
      been fully processed.
    """
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
