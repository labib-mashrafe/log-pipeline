import os
import sqlite3
from parse import parse_line

def load(log_file, db_file):
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, source_file TEXT, line_number INTEGER, ts TEXT, ip TEXT, user TEXT, event TEXT, raw TEXT, UNIQUE(source_file, line_number))")

    with open(log_file) as f:
        lines = f.readlines()

    source = os.path.basename(log_file)
    count = 0
    for line_number, line in enumerate(lines, start=1):
        result = parse_line(line)
        if result is not None:
            cur.execute("INSERT OR IGNORE INTO events (source_file, line_number, ts, ip, user, event, raw) VALUES (?, ?, ?, ?, ?, ?, ?)", (source, line_number, result["ts"], result["ip"], result["user"], result["event"], result["raw"]))
            count = count + 1

    conn.commit()
    conn.close()
    return count

if __name__ == "__main__":
    count = load("data/OpenSSH_2k.log", "data/events.db")
    print("inserted", count)