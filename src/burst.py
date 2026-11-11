import sqlite3

THRESHOLD = 10
conn = sqlite3.connect("data/events.db")
rows = conn.execute(
    "SELECT ip, substr(ts, 12, 2) AS hour, COUNT(*) AS failures "
    "FROM events WHERE event = 'failed_password' "
    "GROUP BY ip, hour HAVING COUNT(*) >= ? ORDER BY failures DESC",
    (THRESHOLD,)
).fetchall()
for ip, hour, failures in rows:
    print("FLAGGED", ip, "hour", hour, "failures", failures)
conn.close()