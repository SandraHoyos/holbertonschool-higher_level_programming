#!/usr/bin/python3
"""First Rectangle"""

from models.base import Base


class Rectangle(Base):
    """A rectangle class that inherits from
    the base class
    Args:
        Base(model): the inherited model
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructs the rectange's attributes
        Args:
            height(int): rectangle's height
            width(int): rectangle's width
            x(int): input value
            y(int): input value
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the Width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the Width (private) of the rectangle
        Args:
            value(int): value of the rectangle
        """
        self.__width = value

    @property
    def height(self):
        """Gets the height (private) of the rectangle"""
        return self.__height

    @width.setter
    def height(self, value):
        """Sets the height(private) of the rectangle
          Args:
            value(int): value of the rectangle
        """
        self.__height = value

    @property
    def x(self):
        """Gets the x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x value
         Args:
            value(int): x value
        """
        self.__x = value

    @property
    def y(self):
        """Gets the x value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y value
         Args:
            value(int): y value
        """
        self.__y = value
