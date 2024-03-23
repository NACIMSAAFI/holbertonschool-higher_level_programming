#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

db = MySQLdb.connect(
    host="localhost", port=3306, user=argv[1], db=argv[3], charset="utf8"
)
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
for row in cursor.fetchall():
    print(row)
cursor.close()
db.close()
