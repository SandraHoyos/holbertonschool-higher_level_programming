#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for j in range(x):
            print("{:d}".format(my_list[j]), end="")
            i += 1
    except IndexError:
        pass
    print()
    return i