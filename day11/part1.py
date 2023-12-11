with open('input') as f:
    map = [list(line.rstrip()) for line in f]


def transpose(l):
    return [list(x) for x  in zip(*l)]


def expand_down(l):
    output = []
    for row in l:
        output.append(row)
        if row.count('.') == len(row):
            output.append(row)
    return output


def scan_galaxies(l):
    galaxies = []
    for y, row in enumerate(l):
        for x, char in enumerate(row):
            if char == '#':
                galaxies.append((x, y))
    return galaxies


def manhatten_distance(first, second):
    return abs(first[0]-second[0]) + abs(first[1]-second[1])


def list_product(l):
    product = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            product.append([l[i], l[j]])
    return product


map = expand_down(map)
map = transpose(map)
map = expand_down(map)
map = transpose(map)

galaxies = scan_galaxies(map)
pairs = list_product(galaxies)

sum = 0
for pair in pairs:
    sum += manhatten_distance(pair[0], pair[1])
print(sum)
