import sqlite3

conn = sqlite3.connect("data/events.db")
cur = conn.cursor()
cur.execute("SELECT ip, COUNT(*), MIN(ts), MAX(ts) FROM events WHERE event = 'failed_password' GROUP BY ip HAVING COUNT(*) >= 20 ORDER BY COUNT(*) DESC")
for row in cur.fetchall():
    print("FLAGGED:", row[0], "count:", row[1], "first:", row[2], "last:", row[3])
conn.close()