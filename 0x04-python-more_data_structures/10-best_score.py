#!/usr/bin/python3


def best_score(a_dictionary):
    score = 0
    if a_dictionary is None:
        return (None)
    for x in a_dictionary:
        if a_dictionary[x] > score:
            score = a_dictionary[x]
            high = x
    return (high)

