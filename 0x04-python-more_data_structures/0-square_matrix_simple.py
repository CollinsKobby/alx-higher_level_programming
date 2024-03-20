#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for slist in matrix:
        m_matrix = []
        for i in slist:
            m_matrix.append(i**2)
        sq_matrix.append(m_matrix)
    return sq_matrix
