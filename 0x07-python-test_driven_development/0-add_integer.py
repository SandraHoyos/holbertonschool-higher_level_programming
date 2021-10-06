#!/usr/bin/python3

"""adds 2 integers"""


del add_integer(a, b=98):
    """adds 2 integers
    returns the addition of
    a and b, or an error if a and b
    are not integers or floats"""

    if type(a) is not [int, float]:
        raise TypeError("a must be an integer")
    if type(b) is not [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
