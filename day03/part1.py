input = open('input', 'r')
lines = input.readlines()

checked = {}

def get_char(coord):
  return lines[coord[1]][coord[0]]

def is_special_character(char):
  if char == ".":
    return False
  if char.isnumeric():
    return False
  return True

def get_neighbors(coord):
  list = []
  for y in range(-1, 2):
    for x in range(-1, 2):
      if x == 0 and y == 0:
        continue
      list.append((coord[0]+x,coord[1]+y))
  return list

def find_whole_word(coord):
  y = coord[1]
  min_x = coord[0]
  max_x = coord[0]

  checked[(min_x, y)] = True

  while lines[y][min_x-1].isnumeric():
    min_x -= 1
    checked[(min_x, y)] = True
  while lines[y][max_x+1].isnumeric():
    max_x += 1
    checked[(max_x, y)] = True
  return lines[y][min_x:max_x+1]

total = 0

for y, line in enumerate(lines):
  for x, char in enumerate(line.strip()):
    if is_special_character(char):
      neighbors = get_neighbors((x, y))
      for neighbor in neighbors:
        if neighbor in checked:
          continue
        char = get_char(neighbor)
        if char.isnumeric():
          word = find_whole_word(neighbor)
          total += int(word)

print(total)