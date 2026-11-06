import sqlite3
import sys

sys.path.insert(0, "src")
from db import load


def test_loading_twice_gives_same_row_count(tmp_path):
    db_file = str(tmp_path / "test.db")
    load("data/OpenSSH_2k.log", db_file)
    load("data/OpenSSH_2k.log", db_file)
    conn = sqlite3.connect(db_file)
    rows = conn.execute("SELECT COUNT(*) FROM events").fetchone()[0]
    conn.close()
    assert rows == 633