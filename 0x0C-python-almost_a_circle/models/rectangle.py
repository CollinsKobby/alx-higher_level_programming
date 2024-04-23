#!/usr/bin/python3
""" A module of a class called Base """
from models.base import Base

class Rectangle(Base):
    """ A class called Rectangle thats nheriting fron the
    class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if 0 > value:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ To calculate the area of the rectangle """
        return self.__height * self.__width

    def display(self):
        """ To display the rectangle using # according to the
        size provided """
        res = ' ' * self.__x
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print("{}{}".format(res, '#' * self.__width))

    def __str__(self):
        """ used to override to return in a different way """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Update the attributes of the rectangle """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]

        if kwargs:
            if args is not None:
                pass
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Represents dictionary represenation of the rectangle """
        dict_res = {}
        dict_res["x"] = self.__x
        dict_res["y"] = self.__y
        dict_res["id"] = self.id
        dict_res["height"] = self.__height
        dict_res["width"] = self.__width
        return dict_res
