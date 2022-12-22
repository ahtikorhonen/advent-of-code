X = [l.strip() for l in open("day-8/input-8.txt")]

ROWS = len(X)
COLUMNS = len(X[0])
p1 = ROWS*COLUMNS - (ROWS - 2)*(COLUMNS - 2)
scores = []

for col in range(1, ROWS - 1):
    for row in range(1, COLUMNS - 1):

        tree = int(X[col][row])
        left = [int(i) for i in X[col][:row]]
        right = [int(i) for i in X[col][row + 1:]]
        up = [int(i[row]) for i in X[:col]]
        down = [int(i[row]) for i in X[col + 1:]]
        left.reverse(), up.reverse()

        # --- puzzle 1 ---
        neighbours_max = [max(left), max(right), max(up), max(down)]
        if tree > min(neighbours_max):
            p1 += 1

        # --- puzzle 2 ---
        line_score = 1
        for line in (left, right, up, down):
            score = 0
            for i in line:
                if i < tree:
                    score += 1
                elif i >= tree:
                    score += 1
                    break
            line_score *= score

        scores.append(line_score)

p2 = max(scores)