import sqlite3
from detect import burst_rows, username_rows, THRESHOLD

conn = sqlite3.connect("data/events.db")
bursts = burst_rows(conn, THRESHOLD)
users = username_rows(conn)
conn.close()

print("LOG REPORT")
print("Threshold:", THRESHOLD, "failed passwords per IP per hour")
print("Flagged IP-hours:", len(bursts))
print("IPs with failed passwords:", len(users))