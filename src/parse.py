import re

ASSUMED_YEAR = 2025
MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, 
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}


def parse_line(line):
    if "Failed password" in line:
        event = "failed_password"
    elif "Invalid user" in line:
        event = "invalid_user"
    else:
        return None
    m = re.search(r"(\S+) from (\d+\.\d+\.\d+\.\d+)", line)
    if m is None:
        return None
    pieces = line.split()
    month = MONTHS[pieces[0]]
    day = int(pieces[1])
    ts = str(ASSUMED_YEAR) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2) + " " + pieces[2]
    return {"ts": ts, "ip": m.group(2), "user": m.group(1), "event": event, "raw": line.strip()}

if __name__ == "__main__":
    with open("data/OpenSSH_2k.log") as f:
        lines = f.readlines()

    parsed = 0
    rejected = 0
    rejected_lines = []
    for line in lines:
        result = parse_line(line)
        if result is None:
            rejected = rejected + 1
            rejected_lines.append(line)
        else:
            parsed = parsed + 1
    print("parsed:", parsed, "rejected:", rejected)
    with open("data/rejected.txt", "w") as out:
        for line in rejected_lines:
            out.write(line)

    missed = 0
    for line in rejected_lines:
        if "Failed password" in line or "Invalid user" in line:
            missed = missed + 1
    print("important lines rejected:", missed)
    if missed > 0:
        print("ERROR: parser rejected", missed, "important lines. Look in data/rejected.txt")
        raise SystemExit(1)

    