import sqlite3
from detect import burst_rows, username_rows, totals, THRESHOLD

conn = sqlite3.connect("data/events.db")
bursts = burst_rows(conn, THRESHOLD)
users = username_rows(conn)
events, failed = totals(conn)
conn.close()

print("LOG REPORT")
print("Threshold:", THRESHOLD, "failed passwords per IP per hour")
print("Flagged IP-hours:", len(bursts))
print("IPs with failed passwords:", len(users))
print("Events stored:", events)
print("Failed passwords:", failed)

user_counts = {}
for ip, count, _ in users:
    user_counts[ip] = count

print()
print("FLAGGED IP-HOURS")
for ip, hour, failures in bursts:
    print(ip, "hour", hour, "failures", failures, "usernames_all_day", user_counts[ip])