import re
import string
from copy import deepcopy

with open('day-5/input-5.txt') as f:
    lines = f.readlines()

# parse input to type [['A', 'F', 'Y'], ...] where sublist is stack ordered from top to bottom
stacks = []
lines_90 = list(zip(*reversed(lines[:8])))
for line in lines_90:
    substack = []
    for item in enumerate(line):
        if item[1] in string.ascii_uppercase:
            substack.append(item[1])
    if substack != []:
        substack.reverse()
        stacks.append(substack)

stacks_p1 = deepcopy(stacks)
stacks_p2 = deepcopy(stacks)

commands = [line.strip() for line in lines[10:]]

for command in commands:
    num, from_stack, to_stack = [int(l) for l in re.findall('\d+', command)]
    #sort puzzle 1
    for i in range(num):
        item = stacks_p1[from_stack - 1][0]
        stacks_p1[from_stack - 1].remove(item)
        stacks_p1[to_stack - 1].insert(0, item)
    # sort puzzle 2
    items = stacks_p2[from_stack - 1][:num]
    del stacks_p2[from_stack - 1][:num]
    stacks_p2[to_stack - 1] = items + stacks_p2[to_stack - 1]
    items = []

# print solutions
print(''.join([x[0] for x in stacks_p1]))
print(''.join([x[0] for x in stacks_p2]))