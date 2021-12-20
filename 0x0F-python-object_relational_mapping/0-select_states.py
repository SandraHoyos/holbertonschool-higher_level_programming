#!/usr/bin/python3
"""
This script is listing all states from the database
hbtn_0e_0_usa

"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
