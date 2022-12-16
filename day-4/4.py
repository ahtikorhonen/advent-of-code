import re

X = [l.strip() for l in open("day-4/input-4.txt")]
lines_split = [re.split(r"[,-]", line) for line in X]
# convert input from ['1-2,2-4', ...] to [[1, 2, 2, 4], ...]
lines_converted = [[int(i) for i in sublist] for sublist in lines_split]

# answer to puzzle 1
num_of_subsets = len(
    [
        line
        for line in lines_converted
        if line[0] <= line[2] <= line[3] <= line[1]
        or line[2] <= line[0] <= line[1] <= line[3]
    ]
)
print(num_of_subsets)

# answer to puzzle 2
num_of_overlaps = len(
    [line for line in lines_converted if line[0] <= line[3] and line[2] <= line[1]]
)
print(num_of_overlaps)
