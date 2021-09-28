#!/usr/bin/python3

"""Defines class Square with private attribute size and validates size"""


class Square:
    """ class square"""

    def __init__(self, size=0):
        """initialization of the class square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
