X = [l.strip() for l in open("day-6/input-6.txt")][0]

def find_unique(str_len: str) -> int:
    substrings = [set(X[i: i + str_len]) for i in range(len(X))]
    unique_members = [1 if len(l) == str_len else 0 for l in substrings]
    return unique_members.index(1) + str_len

p1 = find_unique(4)
p2 = find_unique(14)