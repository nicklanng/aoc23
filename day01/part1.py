input = open('input', 'r')
lines = input.readlines()

total = 0

for line in lines:
  number = ''
  for character in line:
    if character.isnumeric():
      number += character
      break
  for character in reversed(line):
    if character.isnumeric():
      number += character
      break

  total += int(number)

print(total)