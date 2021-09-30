   return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that returns
        the rectangle area
        """
        rectangle_area = self.__height * self.__width
        return rectangle_area

    def perimeter(self):
        """Public instance method that returns the
        rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        rectangle_params = ((2 * self.__height) + (2 * self.__width))
        return rectangle_params

    def __str__(self):
        """Returns the rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))
