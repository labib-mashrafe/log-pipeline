import sqlite3
import sys

sys.path.insert(0, "src")
from db import load
from detect import burst_rows


def test_loading_twice_gives_same_row_count(tmp_path):
    db_file = str(tmp_path / "test.db")
    load("data/OpenSSH_2k.log", db_file)
    load("data/OpenSSH_2k.log", db_file)
    conn = sqlite3.connect(db_file)
    rows = conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]
    conn.close()
    assert rows == 633
def test_identical_lines_at_different_positions_are_both_stored(tmp_path):
    line = "Dec 10 07:27:52 LabSZ sshd[1234]: Failed password for root from 1.2.3.4 port 22 ssh2\n"
    log_file = tmp_path / "two_same.log"
    log_file.write_text(line + line)
    db_file = str(tmp_path / "test.db")
    load(str(log_file), db_file)
    conn = sqlite3.connect(db_file)
    rows = conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]
    conn.close()
    assert rows == 2

def test_burst_flags_only_the_attacker(tmp_path):
    lines = ""
    for i in range(12):
        lines = lines + "Dec 10 12:30:" + str(10 + i) + " LabSZ sshd[1234]: Failed password for root from 203.0.113.5 port 22 ssh2\n"
    lines = lines + "Dec 10 12:40:00 LabSZ sshd[1234]: Failed password for root from 203.0.113.9 port 22 ssh2\n"
    log_file = tmp_path / "burst.log"
    log_file.write_text(lines)
    db_file = str(tmp_path / "test.db")
    load(str(log_file), db_file)
    conn = sqlite3.connect(db_file)
    flagged = burst_rows(conn, 10)
    conn.close()
    assert len(flagged) == 1
    assert flagged[0][0] == "203.0.113.5"
    assert flagged[0][2] == 12