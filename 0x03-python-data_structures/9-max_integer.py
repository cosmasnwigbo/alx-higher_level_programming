#!/usr/bin/python3


def max_integer(my_list=[]):
    mx = 0
    if len(my_list) == 0:
        return (None)
    else:
        for x in range(len(my_list)):
            if my_list[x] >= 0 and my_list[x] >  mx:
                mx = my_list[x]
            elif my_list[x] < 0:
                if mx > my_list[x]:
                    mx = my_list[x]
    return (mx)
