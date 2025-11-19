#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square(x):
        return x ** 2
    return [[square(value) for value in row] for row in matrix]
