#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cnt = 0
    nb_print = 0
    for cnt in range(0, x):
        try:
            print("{}".format(my_list[cnt]), end="")
            nb_print += 1
        except:
            break
    print()
    return nb_print

