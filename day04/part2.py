input = open('input', 'r')
lines = input.readlines()

total = 0
counts = [1]*len(lines)

def get_winners(game):
    tokens = game.split()
    winners = tokens[2:12]
    numbers = tokens[13:38]
    intersection = list(set(winners) & set(numbers))
    return len(intersection)

for y, line in enumerate(lines):
    total += counts[y]
    winners = get_winners(line)
    for i in range(y+1,y+1+winners):
        counts[i] += counts[y]

print(total)