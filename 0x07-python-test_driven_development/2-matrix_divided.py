#!/usr/bin/python3
"""
This module is composed by a function the divides the values of a list
by a given integer of float List must be a list of integers or floats
"""


def matrix_divided(matrix, div):
    """ This functions divides the members of a list by a given value
    Args:
    matrix - the list
    div - divisor
    Returns a new matrix """
    size = len(matrix[0])
    sq_matrix = []
    for lis in matrix:
        n_matrix = []
        if len(lis) != size:
            raise TypeError("Each row of the matrix must have the same size")
        if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        for i in lis:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            n_l = round(i / div, 2)
            n_matrix.append(n_l)
        sq_matrix.append(n_matrix)
    return (sq_matrix)
