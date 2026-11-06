import sqlite3
from parse import parse_line

conn = sqlite3.connect("data/events.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, source_file TEXT, line_number INTEGER, ts TEXT, ip TEXT, user TEXT, event TEXT, raw TEXT, UNIQUE(source_file, line_number))")

with open("data/OpenSSH_2k.log") as f:
    lines = f.readlines()

SOURCE = "OpenSSH_2k.log"
count = 0
for line_number, line in enumerate(lines, start=1):
    result = parse_line(line)
    if result is not None:
        cur.execute("INSERT OR IGNORE INTO events (source_file, line_number, ts, ip, user, event, raw) VALUES (?, ?, ?, ?, ?, ?, ?)", (SOURCE, line_number, result["ts"], result["ip"], result["user"], result["event"], result["raw"]))
        count = count + 1

conn.commit()
conn.close()
print("inserted", count)