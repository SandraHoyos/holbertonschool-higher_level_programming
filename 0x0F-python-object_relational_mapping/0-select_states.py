#!/usr/bin/python3
"""This script is listing all states
from the database hbtn_0e_0_usa order by id
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    c = conn.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    conn.close()
