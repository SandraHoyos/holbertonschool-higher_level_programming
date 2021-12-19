#!/usr/bin/python3
"""
script to list all states from db hbtn_0e_usa
takes 3 args username, mysql passwd, db name
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], database=argv[3], charset="utf8")
    c = conn.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    conn.close()