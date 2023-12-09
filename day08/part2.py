import re
from math import lcm

with open('input') as f:
    lines = [line.rstrip() for line in f]

instructions = lines[0]
paths = {}
nodes = {}

for i in range (2, len(lines)):
    line = re.sub('[=(\)\,]', '', lines[i])
    tokens = line.split()
    paths[tokens[0]] = (tokens[1], tokens[2])
    if tokens[0][2] == 'A':
        nodes[tokens[0]] = 0

for k in nodes.keys():
    step = 0
    node = k
    while True:
        instruction = instructions[step%len(instructions)]
        if instruction == 'L':
            node = paths[node][0]
        else:
            node = paths[node][1]
        step += 1
        if node[2] == 'Z':
            break
    nodes[k] = step
steps = list(nodes.values())
print(lcm(*steps))