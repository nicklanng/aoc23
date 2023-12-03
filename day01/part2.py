input = open('input', 'r')
lines = input.readlines()

total = 0

words = [
  "zero",
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine"
]

def searchNumber(word_buffer):
  for i, number in enumerate(words):
    if word_buffer[-len(number):] == number:
      return i
  return -1


for line in lines:
  numbers = []

  word_buffer = ''

  for character in line.strip():
    if character.isnumeric():
      numbers.append(int(character))
    else:
      word_buffer += character
      number = searchNumber(word_buffer)
      if number > -1:
        numbers.append(number)
    
  total += numbers[0]*10 + numbers[-1]

print(total)

