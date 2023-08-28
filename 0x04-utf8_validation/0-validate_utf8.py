#!/usr/bin/python3

def validUTF8(data):
    """ determines if a given set represents a valid
    UTF-8 encoding
    """
    if not data:
        return False

    for val in data:
        if (val >> 7) != 0:
            return False
    return True
