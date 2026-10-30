# Log Pipeline and Detector

A small Python and SQLite project that parses an SSH server log and flags suspicious activity. A learning project.

## Data

- Source: Loghub OpenSSH 2k sample, https://github.com/logpai/loghub/tree/master/OpenSSH
- Download: https://raw.githubusercontent.com/logpai/loghub/master/OpenSSH/OpenSSH_2k.log
- Save it as data/OpenSSH_2k.log. The log file is not included in this repo.
- Terms (quoted from the Loghub README): "The datasets are freely available for research or academic work. For any usage or distribution of the datasets, please refer to the loghub repository URL https://github.com/logpai/loghub and cite the loghub paper where applicable."
- Citation 1: Jieming Zhu, Shilin He, Pinjia He, Jinyang Liu, Michael R. Lyu. "Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics". IEEE ISSRE, 2023.
- Citation 2: Zhihan Jiang, Jinyang Liu, Junjie Huang, Yichen Li, Yintong Huo, Jiazhen Gu, Zhuangbin Chen, Jieming Zhu, Michael R. Lyu. "A Large-scale Evaluation for Log Parsing Techniques: How Far are We?". ACM ISSTA, 2024.

## Status

## Week 1: what works so far
- Reads the OpenSSH log and parses two line types (Failed password, Invalid user) with a regex
- Pulls out timestamp, IP, username and event type
- Tested on the first 50 lines only. Not run on the full 2000 lines yet
- Not built yet: database, detector
