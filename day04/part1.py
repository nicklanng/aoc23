input = open('input', 'r')
lines = input.readlines()

total = 0

for line in lines:
    tokens = line.split()
    winners = tokens[2:12]
    numbers = tokens[13:38]

    intersection = list(set(winners) & set(numbers))
    if len(intersection) > 0:
        total += 1 << len(intersection)-1

print(total)