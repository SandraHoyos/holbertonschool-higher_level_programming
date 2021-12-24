#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
usin 3 arguments: user, password and database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()