#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    if len(tuple_a) > 2 or len(tuple_b) > 2:
        for x in range(2):
            tuple_c += (tuple_a[x] + tuple_b[x],)
    else:
        tuple_a += (0, 0)
        tuple_b += (0, 0)
        for x in range(2):
            tuple_c += (tuple_a[x] + tuple_b[x],)
    return (tuple_c)
