#!/usr/bin/python3

"""Defines class square with private attribute"""


class Square:
    """class square definition"""
    def __init__(self, size=0):
        """"inicializes square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns area the square"""
        return (self.__size)**2
