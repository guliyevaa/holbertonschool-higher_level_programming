#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = lambda x: x ** 2
    return [[square(value) for value in row] for row in matrix]
