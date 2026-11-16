import sqlite3

THRESHOLD = 10

def burst_rows(conn, threshold):
    return conn.execute(
        "SELECT ip, substr(ts, 12, 2) AS hour, COUNT(*) AS failures "
        "FROM events WHERE event = 'failed_password' "
        "GROUP BY ip, hour HAVING COUNT(*) >= ? ORDER BY failures DESC",
        (threshold,)
    ).fetchall()

def username_rows(conn):
    return conn.execute(
        "SELECT ip, COUNT(DISTINCT user) AS users, COUNT(*) AS failures "
        "FROM events WHERE event = 'failed_password' "
        "GROUP BY ip ORDER BY users DESC",
    ).fetchall()

if __name__ == "__main__":
    conn = sqlite3.connect("data/events.db")
    print("BURSTS, threshold", THRESHOLD)
    for ip, hour, failures in burst_rows(conn, THRESHOLD):
        print("FLAGGED", ip, "hour", hour, "failures", failures)
    print("USERNAMES PER IP")
    for ip, users, failures in username_rows(conn):
        print(ip, "users", users, "failures", failures)
    conn.close()