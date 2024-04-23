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
