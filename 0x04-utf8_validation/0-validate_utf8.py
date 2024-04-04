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
    count_ones = 0
    for num in data:
        # Extract the 8 least significant bits
        num &= 0xff
        if count_ones == 0:
            # First byte of a character
            if num >= 0xc0:
                if num >= 0xf0:
                    count_ones = 4
                elif num >= 0xe0:
                    count_ones = 3
                elif num >= 0xc2:
                    count_ones = 2
                else:
                    return False
            else:
                # Valid single-byte character
                count_ones = 0
        else:
            # Subsequent bytes of a character
            if num < 0x80 or num >= 0xc0:
                return False
            count_ones -= 1
    return count_ones == 0
