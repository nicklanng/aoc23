with open('input') as f:
    lines = [line.rstrip() for line in f]


def is_section_count_valid(input, counts):
    ranges = list(filter(None, input.split('.')))
    if len(ranges) != len(counts):
        return False
    for i, range in enumerate(ranges):
        if len(range) != counts[i]:
            return False
    return True


def count_unknowns(input):
    return input.count('?')


def replace_unknowns(input, binary):
    j = 0
    new_str = ''
    for char in input:
        if char == '?':
            if binary[j] == '0':
                new_str += '.'
            else:
                new_str += '#'
            j += 1
        else:
            new_str += char
    return new_str


total = 0
for line in lines:
    tokens = line.split()
    gears = tokens[0]
    counts = [int(x) for x in tokens[1].split(",")]

    unknowns = count_unknowns(gears)
    possibilities = 1<<unknowns

    for i in range(possibilities):
        binary = bin(i)[2:].rjust(unknowns, '0')
        possible_gears = replace_unknowns(gears, binary)
        if is_section_count_valid(possible_gears, counts):
            total += 1
print(total)