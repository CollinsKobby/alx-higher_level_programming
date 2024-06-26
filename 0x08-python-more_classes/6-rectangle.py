#!/usr/bin/python3
""" A module of a class Rectangle
"""


class Rectangle:
    """ A Rectangle class that takes in the height and the width of
    the rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """ Calculates the area of the rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """ Calculates the perimeter of the rectangle
        if height or width = 0, then perimeter = 0
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """ Used to print the character #
        """
        result = ''
        for i in range(self.__height):
            result += '#' * self.__width
            if i != self.__height - 1:
                result += '\n'
        return (result)

    def __repr__(self):
        """ return a string representation of the rectangle to be able to
        recraete a new instance by using eval()
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Deletes a rectangle
        return: Bye rectangle...
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
