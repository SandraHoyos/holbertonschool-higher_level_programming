#!/usr/bin/python3
import MySQLdb
from sys import argv
conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                       passwd=argv[2], db="hbtn_0e_0_usa", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER by id ASC",
            (argv[4],))
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
