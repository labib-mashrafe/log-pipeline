import sqlite3
from parse import parse_line

conn = sqlite3.connect("data/events.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, ts TEXT, ip TEXT, user TEXT, event TEXT, raw TEXT)")
cur.execute("DELETE FROM events")

with open("data/OpenSSH_2k.log") as f:
    lines = f.readlines()

count = 0
for line in lines:
    result = parse_line(line)
    if result is not None:
        cur.execute("INSERT INTO events (ts, ip, user, event, raw) VALUES (?, ?, ?, ?, ?)", (result["ts"], result["ip"], result["user"], result["event"], result["raw"]))
        count = count + 1

conn.commit()
conn.close()
print("inserted", count)