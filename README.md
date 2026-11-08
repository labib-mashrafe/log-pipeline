# Log Pipeline and Detector

A small Python and SQLite project that parses an SSH server log and flags suspicious activity. A learning project.

## Data

- Source: Loghub OpenSSH 2k sample, https://github.com/logpai/loghub/tree/master/OpenSSH
- Download: https://raw.githubusercontent.com/logpai/loghub/master/OpenSSH/OpenSSH_2k.log
- Save it as data/OpenSSH_2k.log. The log file is not included in this repo.
- Terms (quoted from the Loghub README): "The datasets are freely available for research or academic work. For any usage or distribution of the datasets, please refer to the loghub repository URL https://github.com/logpai/loghub and cite the loghub paper where applicable."
- Citation 1: Jieming Zhu, Shilin He, Pinjia He, Jinyang Liu, Michael R. Lyu. "Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics". IEEE ISSRE, 2023.
- Citation 2: Zhihan Jiang, Jinyang Liu, Junjie Huang, Yichen Li, Yintong Huo, Jiazhen Gu, Zhuangbin Chen, Jieming Zhu, Michael R. Lyu. "A Large-scale Evaluation for Log Parsing Techniques: How Far are We?". ACM ISSTA, 2024.

## Known limits
- The log has no year, so I guessed 2025 in the constant ASSUMED_YEAR at the top of src/parse.py.
- The server timezone is unknown, so I can't compare these times with times from another server.
- The data covers one day only, 10 Dec from 06:55 to 11:04.

## Week 1: what works so far
- Reads the OpenSSH log and parses two line types (Failed password, Invalid user) with a regex.
- Pulls out timestamp, IP, username and event type.
- Run on all 2000 lines: 633 parsed, 1367 rejected (other line types, saved to data/rejected.txt).
- Not built yet: detector

## Week 2: what works so far
- Timestamps are converted to YYYY-MM-DD HH:MM:SS format, with the year assumed as 2025.
- Events are stored in SQLite’s events table with a unique key of (source_file, line_number), so loading the same file twice gives 633 rows.
- counts.py counts failures per IP and per hour, and the totals add up to 520.
- A pytest test loads the log twice and checks that the events table still contains exactly 633 rows.