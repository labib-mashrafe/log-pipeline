import sqlite3
conn = sqlite3.connect("data/events.db")
cur = conn.cursor()
cur.execute("SELECT ip, COUNT(*) FROM events WHERE event = 'failed_password' GROUP BY ip ORDER BY COUNT(*) DESC LIMIT 5")
for row in cur.fetchall():
    print(row)
conn.close()