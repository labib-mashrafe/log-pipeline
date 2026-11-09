import sqlite3
import sys

conn = sqlite3.connect("data/events.db")
with open(sys.argv[1]) as f:
    sql = f.read()
for row in conn.execute(sql):
    print(row)
conn.close()