input = open('input', 'r')
lines = input.readlines()

max_values = (12, 13, 14)

def get_game_counts(game):
  counts = [0, 0, 0]
  results = x = game.strip().split(": ")[1]
  hands = x = results.split("; ")
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

def is_game_valid(counts):
  return counts[0] <= max_values[0] and counts[1] <= max_values[1] and counts[2] <= max_values[2]

total = 0
for i, line in enumerate(lines):
  counts = get_game_counts(line)
  if is_game_valid(counts):
    total += (i+1)
print(total)