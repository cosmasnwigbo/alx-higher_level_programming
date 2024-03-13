#!/usr/bin/python3
# print_last_digit(number) - a function that prints the last digit of a number
# @number parameter of function print_last_digit


def print_last_digit(number):
    if (number >= 0):
        number = (number) % 10
        print(number, end="")
    else:
        number = abs(number) % 10
        print(number, end="")
    return (number)
