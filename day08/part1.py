import re

with open('input') as f:
    lines = [line.rstrip() for line in f]

instructions = lines[0]
paths = {}

for i in range (2, len(lines)):
    line = re.sub('[=(\)\,]', '', lines[i])
    tokens = line.split()
    paths[tokens[0]] = (tokens[1], tokens[2])

node = 'AAA'
target = 'ZZZ'
step = 0
while True:
    instruction = instructions[step%len(instructions)]
    if instruction == 'L':
        node = paths[node][0]
    else:
        node = paths[node][1]
    step += 1
    if node == target:
        break
print(step)