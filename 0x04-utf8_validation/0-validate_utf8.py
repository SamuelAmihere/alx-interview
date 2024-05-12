#!/usr/bin/python3
"""
UTF-8 Validation:
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid
    UTF-8 encoding.

    data: list of integers
    """
    if not data or len(data) == 0:
        return False

    n_bytes = 0
    i = 0

    while i < len(data):
        num = data[i]

        if type(num) != int or num < 0 or num > 0x10ffff:
            return False

        bin_rep = format(num, '#010b')[-8:]

        if n_bytes == 0:
            j = 0
            while j < len(bin_rep):
                # Count the number of 1s in the beginning of the string.
                # E.g. '11110xxx' should return 4
                if bin_rep[j] == '0':
                    break
                n_bytes += 1
                j += 1

            if n_bytes == 0:
                i += 1
                continue

            if n_bytes == 1 or n_bytes > 4:
                # UTF-8 characters are between 2 and 4 bytes long
                return False
        else:
            # check if the most significant bit is 1 and the second one is 0
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        # Decrease the number of bytes to process
        n_bytes -= 1
        i += 1

    return n_bytes == 0
