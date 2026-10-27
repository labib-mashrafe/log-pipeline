with open("data/OpenSSH_2k.log") as f:
    lines = f.readlines()

print(len(lines))

for line in lines[:10]:
    print(line.strip())