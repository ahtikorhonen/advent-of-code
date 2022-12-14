with open('day-2/input-2.txt') as f:
    #read input from textfile
    lines = f.readlines()
    lines_sliced = [line[:3] for line in lines]

outcomes_part1 = {
    'A Z': 0,
    'A X': 3,
    'A Y': 6,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C Y': 0,
    'C Z': 3,
    'C X': 6
}

shapes = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

points = [outcomes_part1[line] + shapes[line[2]] for line in lines_sliced]
# puzzle 1 answer
print(sum(points))

outcomes_part2 = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

def map_to_points(line: str) -> int:
    result = line[2]
    for i, key in enumerate(outcomes_part1):
        if key[0] == line[0] and outcomes_part1[key] == outcomes_part2[result]:
            return outcomes_part2[result] + shapes[key[2]]

points_unencrypted = map(map_to_points, lines_sliced)
print(sum(points_unencrypted))
