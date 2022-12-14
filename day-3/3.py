import string

X = [l.strip() for l in open('day-3/input-3.txt')]

# split strings in half and create a tuple
lines_split = [(line[:len(line)//2], line[len(line)//2:]) for line in X]

# find common characters in tuples
common_characters = [
    ''.join(set(line[0]).intersection(line[1])) for line in lines_split
    ]

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
alphabet_index = [i + 1 for i in range(0, len(alphabet))]
alphabet_dict = dict(zip(alphabet, alphabet_index))

priorities = [alphabet_dict[char] for char in common_characters]
# answer to puzzle 1
priority_sum = sum(priorities)

# group lines to sets of 3
lines_grouped = [X[i:i+3] for i in range(0, len(X), 3)]

# find common elements between these 3 lines
common_in_lines_grouped = [
        set.intersection(*map(set, list(strings))).pop() for strings in lines_grouped
    ]
# map common elements to priority values
priorities2 = [alphabet_dict[char] for char in common_in_lines_grouped]
# answer to puzzle 2
priority_sum2 = sum(priorities2)