#!/usr/bin/python3
"""
script to list all states from db hbtn_0e_usa
takes 3 args username, mysql passwd, db name
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    lst = c.fetchall()
    for r in lst:
        print(r)
    c.close()
    db.close()