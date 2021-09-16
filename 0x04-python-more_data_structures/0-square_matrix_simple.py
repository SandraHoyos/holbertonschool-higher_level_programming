#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for elem in matrix:
        return[(list(map((lambda num : num ** 2), elem)))]
