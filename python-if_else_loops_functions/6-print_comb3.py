#!/usr/bin/python3

for i in range(0, 9):
    for j in range(i + 1, 9 + 1):
        if i * 10 + j != 89:
            print("{:d}{:d}".format(i, j), end=", ")
print("89")
