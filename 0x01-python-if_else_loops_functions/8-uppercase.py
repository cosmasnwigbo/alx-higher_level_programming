#!/usr/bin/python3
# uppercase(str) - function that prints a string in uppercase
# @str: parameter of function 
# Return: str


def uppercase(str):
    i = 0
    for x in (str):
        if ord('a') <= ord(x) <= ord('z'):
            i = ord(x) - 32
        else:
            i = ord(x)
        print(chr(i), end="")
    print()

