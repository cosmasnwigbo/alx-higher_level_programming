#!/usr/bin/python3
# def add(a, b) - a function that adds two integers
# @(a, b) parameter of function add
# Return: a+b


def add(a, b):
    if (b >= 0):
        return a + b
    else:
        b = abs(b)
        return a - b
