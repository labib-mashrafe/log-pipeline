with open("data/OpenSSH_2k.log") as f:
    lines = f.readlines()

print(len(lines))

for line in lines[:50]:
    print(line.strip())

count = 0
for line in lines[:50]:
    if "Failed password" in line:
        count = count + 1
        print(line.strip())
print(count)
example = lines[5]
pieces = example.split()
print(pieces)

print(pieces[12])
example2 = lines[28]
pieces2 = example2.split()
print(pieces2[12])

print(pieces[pieces.index("from") + 1])
print(pieces2[pieces2.index("from") + 1])

for line in lines[:50]:
    if "Failed password" in line:
        pieces = line.split()
        print(pieces[pieces.index("from") + 1])

import re

line = "Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2"
m = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
print(m.group(1))

m2 = re.search(r"(\S+) from (\d+\.\d+\.\d+\.\d+)", line)
print(m2.group(1), m2.group(2))