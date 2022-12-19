from collections import defaultdict

X = [l.strip() for l in open("day-7/input-7.txt")]

SZ = defaultdict(int)

path = []
for line in X:
    words = line.split()
    if words[1] == "cd":
        if words[2] == "..":
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == "ls":
        continue
    elif words[0] == "dir":
        continue
    else:
        sz = int(words[0])
        for i in range(1, len(path) + 1):
            SZ["/".join(path[:i])] += sz

unused_space = 70_000_000 - max(SZ.values())
sz_sorted = dict(sorted(SZ.items(), key=lambda item: item[1]))
p1, p2 = 0, 0

for k, v in sz_sorted.items():
    if v < 100_000:
        p1 += v
    elif v + unused_space >= 30_000_000 and p2 == 0:
        p2 = v

print(p1, p2)