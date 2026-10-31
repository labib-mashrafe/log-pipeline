import re

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
    ts = " ".join(pieces[0:3])
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