#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return[(list(map((lambda num : num ** 2), elem))for elem in matrix)]
