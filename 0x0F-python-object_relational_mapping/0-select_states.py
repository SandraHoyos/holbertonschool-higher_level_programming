#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
usin 3 arguments: user, password and database
"""
import MySQLdb
import sys

if __name__ == "__main__":
   

    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cur = db.cursor()
    query = 'SELECT * FROM states ORDER BY states.id ASC'
    cur.execute(query)
    for row in cur.fetchall():
        print(row)