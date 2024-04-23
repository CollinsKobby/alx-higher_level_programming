#!/usr/bin/python3
""" Module for a square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class called Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Print info about the square """
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ sizeof the square """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update the attributes of the square """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        if kwargs:
            if args is not None:
                pass
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)
