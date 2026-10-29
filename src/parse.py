def parse_line(line):
    if "Failed password" in line:
        event = "failed_password"
    elif "Invalid user" in line:
        event = "invalid_user"
    else:
        return None      
    pieces = line.split()
    ts = " ".join(pieces[0:3])
    ip = pieces[pieces.index("from") + 1]
    user = pieces[pieces.index("from") - 1]
    return {"ts": ts, "ip": ip, "user": user, "event": event, "raw": line.strip()}

with open("data/OpenSSH_2k.log") as f:
    lines = f.readlines()
for line in lines[:50]:
    result = parse_line(line)
    if result is not None:
        print(result["ts"], result["ip"], result["user"], result["event"])