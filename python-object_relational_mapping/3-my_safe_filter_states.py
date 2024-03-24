#!/usr/bin/python3
""" Script takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         db=argv[3])
    c = db.cursor()
    c.execute("SELECT * from states WHERE name LIKE %s ORDER BY states.id",
              (argv[4],))
    for state in c.fetchall():
        print(state)
    c.close()
    db.close()
