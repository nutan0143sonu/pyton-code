import sqlite3 as lite
import sys
con=lite.connect('test.db')
with con:
    cur=con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data=cur.fetchone()

    
