#!/usr/bin/env python3
# fizzbuzz() - function that prints the numbers from 1 to 100


def fizzbuzz():
    for x in range(1, 101):
        if (x % 3 == 0 and x % 5 == 0):
            print("FizzBuzz", end=" ")
        elif (x % 5 == 0):
            print("Buzz", end=" ")
        elif (x % 3 == 0):
            print("Fizz", end=" ")
        else:
            print(x, end=" ")
