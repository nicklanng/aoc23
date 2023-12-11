with open('input') as f:
    map = [list(line.rstrip()) for line in f]


def transpose(l):
    return [list(x) for x  in zip(*l)]


def expand_down(l):
    output = []
    for row in l:
        if row.count('.') + row.count('*') == len(row):
            output.append(['*']*len(row))
        else:
            output.append(row)
    return output


def scan_galaxies(l):
    galaxies = []
    for y, row in enumerate(l):
        for x, char in enumerate(row):
            if char == '#':
                galaxies.append((x, y))
    return galaxies


def manhattan_distance(first, second):
    return abs(first[0]-second[0]) + abs(first[1]-second[1])


def list_product(l):
    product = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            product.append([l[i], l[j]])
    return product


def count_expanded_zone_crossings(first, second):
    lowest_x = min(first[0], second[0])
    highest_x = max(first[0], second[0])
    lowest_y = min(first[1], second[1])
    highest_y = max(first[1], second[1])

    count = 0
    for x in range(lowest_x, highest_x):
        if map[lowest_y][x] == '*':
            count +=1
    for y in range (lowest_y, highest_y):
        if map[y][highest_x] == '*':
            count += 1
    return count


map = expand_down(map)
map = transpose(map)
map = expand_down(map)
map = transpose(map)

galaxies = scan_galaxies(map)
pairs = list_product(galaxies)

sum = 0
for pair in pairs:
    sum += manhattan_distance(pair[0], pair[1])
    sum += count_expanded_zone_crossings(pair[0], pair[1])*(1000000-1)
print(sum)
