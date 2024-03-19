#!/usr/bin/python3

# print_matrix_integer -  a function that prints a matrix of integers
# @matrix: parameter of print_matrix_integer function


def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            print("{:d}".format(y), end=" ")
        print('\n')
