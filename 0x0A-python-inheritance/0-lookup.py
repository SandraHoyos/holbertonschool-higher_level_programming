#!/usr/bin/python3
"""  returns the list of available attributes
methods of an object
"""


def lookup(obj):
    """returns the list of attributes"""
    return dir(obj)
