input = open('input', 'r')
lines = input.readlines()

def get_game_counts(game):
  counts = [0, 0, 0]
  results = game.strip().split(": ")[1]
  hands = results.split("; ")
  for hand in hands:
    colors = hand.split(", ")
    for color in colors:
      [count, name] = color.split()
      match name:
        case "red":
          counts[0] = max(counts[0], int(count))
        case "green":
          counts[1] = max(counts[1], int(count))
        case "blue":
          counts[2] = max(counts[2], int(count))
  return counts

total = 0
for i, line in enumerate(lines):
  counts = get_game_counts(line)
  total += counts[0]*counts[1]*counts[2]

print(total)