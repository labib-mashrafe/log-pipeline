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