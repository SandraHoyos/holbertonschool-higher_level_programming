#!/usr/bin/python3

"""adds 2 integers"""


del add_integer(a, b=98):
    """add 2 integers
    returns the addition of
    a and b, or an error if a or b
    are not integer or float"""

    if type(a) is not [int, float]:
        raise TypeError("a must be an integer")
    if type(b) is not [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
