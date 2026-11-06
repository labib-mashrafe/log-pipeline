from parse import parse_line

counts = {}
with open("data/OpenSSH_2k.log") as f:
    lines = f.readlines()

for line in lines:
    result = parse_line(line)
    if result is not None and result["event"] == "failed_password":
        ip = result["ip"]
        if ip in counts:
            counts[ip] = counts[ip] + 1
        else:
            counts[ip] = 1

print(len(counts))
print(sum(counts.values()))

pairs = []
for ip in counts:
    pairs.append((counts[ip], ip))
pairs.sort(reverse=True)
for pair in pairs[:10]:
    print(pair[1], pair[0])

hours = {}
for line in lines:
    result = parse_line(line)
    if result is not None and result["event"] == "failed_password":
        hour = result["ts"][11:13]
        if hour in hours:
            hours[hour] = hours[hour] + 1
        else:
            hours[hour] = 1

for hour in sorted(hours):
    print(hour, hours[hour])
print(sum(hours.values()))