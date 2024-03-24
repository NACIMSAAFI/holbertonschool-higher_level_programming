#!/usr/bin/python3
""" Script takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(argv[0]))
        exit(1)
    state_name_searched = argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        db=argv[3],
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY\
    '{}' ORDER BY id ASC".format(state_name_searched,))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
