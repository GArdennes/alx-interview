#!/usr/bin/python3
"""
0-validate_utf8
"""


def validUTF8(data):
    """
    Determines if a given dataset represents a valid UTF-8 encoding.

    Args:
      data: A list of integers representing bytes of data.

    Returns:
      True if data is valid UTF-8 encoding, else False.
    """
    count_bytes = 0
    for num in data:
        if count_bytes == 0:
            if (num >> 5) == 0b110:
                count_bytes = 1
            elif (num >> 4) == 0b1110:
                count_bytes = 2
            elif (num >> 3) == 0b11110:
                count_bytes = 3
            elif (num >> 7) != 0:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            count_bytes -= 1
    return count_bytes == 0
