#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cnt = 0
    nb_print = 0
    while cnt < x:
        try:
            print("{}".format(my_list[cnt]), end="")
            nb_print += 1
        except IndexError:
            break
        cnt += 1
    print()
    return nb_print
