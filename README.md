# Log Pipeline and Detector

A small Python and SQLite project that parses an SSH server log and flags suspicious activity. A learning project.

## Data

- Source: Loghub OpenSSH 2k sample, https://github.com/logpai/loghub/tree/master/OpenSSH
- Download: https://raw.githubusercontent.com/logpai/loghub/master/OpenSSH/OpenSSH_2k.log
- Save it as data/OpenSSH_2k.log. The log file is not included in this repo.
- Terms (quoted from the Loghub README): "The datasets are freely available for research or academic work. For any usage or distribution of the datasets, please refer to the loghub repository URL https://github.com/logpai/loghub and cite the loghub paper where applicable."
- Citation 1: Jieming Zhu, Shilin He, Pinjia He, Jinyang Liu, Michael R. Lyu. "Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics". IEEE ISSRE, 2023.
- Citation 2: Zhihan Jiang, Jinyang Liu, Junjie Huang, Yichen Li, Yintong Huo, Jiazhen Gu, Zhuangbin Chen, Jieming Zhu, Michael R. Lyu. "A Large-scale Evaluation for Log Parsing Techniques: How Far are We?". ACM ISSTA, 2024.
- Licence: MIT (my code only, see the LICENSE file). The log data has its own terms, quoted above.

## How to run
Run all commands from the log-pipeline folder.
0. Create a folder named `data` first (on Windows: `mkdir data`), then download the log (see the Data section above) and save it as data/OpenSSH_2k.log
1. Load the log into the database: python src/db.py
2. Print the report: python src/report.py
3. Run the tests (install pytest once first with: pip install pytest): python -m pytest

## Known limits
- The log has no year, so I guessed 2025 in the constant ASSUMED_YEAR at the top of src/parse.py.
- The server timezone is unknown, so I can't compare these times with times from another server.
- The data covers one day only, 10 Dec from 06:55 to 11:04.
- The parser counts only "Failed password" and "Invalid user" lines. Lines like "Failed none" are skipped.
- 1367 of 2000 lines are not parsed because they are other event types, such as pam_unix(sshd:auth): authentication failure and Did not receive identification string. They are saved to data/rejected.txt.
- The username count per IP covers the whole log, not a single hour, so it can't show when an attacker changed usernames.

## Week 1: what works so far
- Reads the OpenSSH log and parses two line types (Failed password, Invalid user) with a regex.
- Pulls out timestamp, IP, username and event type.
- Run on all 2000 lines: 633 parsed, 1367 rejected (other line types, saved to data/rejected.txt).

## Week 2: what works so far
- Timestamps are converted to YYYY-MM-DD HH:MM:SS format, with the year assumed as 2025.
- Events are stored in SQLite’s events table with a unique key of (source_file, line_number), so loading the same file twice gives 633 rows.
- counts.py counts failures per IP and per hour, and the totals add up to 520.
- A pytest test loads the log twice and checks that the events table still contains exactly 633 rows.

## Week 3: what works so far
- Burst threshold: 10 failed passwords from one IP in one hour (THRESHOLD in src/detect.py). The highest IP-hour below it has 7 failures and the lowest flagged one has 16, so small data changes won't flip the result.
- Limit: an attack of 16 failures split 8 and 8 across an hour boundary is missed, though its total exceeds 10.
- Checked by hand: 5.188.10.180 in hour 08 has 18 failed passwords with findstr, same as the query.
- Run it with: python src/detect.py
- Distinct usernames per IP: 187.141.143.180 tried 28 usernames about 2.86 times each, while 183.62.140.253 tried 10 usernames about 28.6 times each. Counting failures alone hides the difference between trying many usernames and repeatedly targeting a smaller set.
