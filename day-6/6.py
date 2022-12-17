X = [l.strip() for l in open("day-6/input-6.txt")][0]

substrings = [set(X[i: i + 4]) for i in range(len(X))]
unique_members = [1 if len(l) == 4 else 0 for l in substrings]

p1 = unique_members.index(1) + 4

substrings2 = [set(X[i: i + 14]) for i in range(len(X))]
unique_members2 = [1 if len(l) == 14 else 0 for l in substrings2]

p2 = unique_members2.index(1) + 14