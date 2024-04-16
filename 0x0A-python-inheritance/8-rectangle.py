#!/usr/bin/python3
""" A module description
A simple class called Rectangle """


class BaseGeometry:
    """ An empty class """
    def area(self):
        """ Area of a shape """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ A simple class called Rectangle that nherits from the
    superclass BaseGeometry
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.__init__(self)
