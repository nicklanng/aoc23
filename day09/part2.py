with open('input') as f:
    lines = [line.rstrip() for line in f]


def all_zero(list):
    return list.count(0) == len(list)


def create_delta(list):
    delta = []
    for previous, current in zip(list, list[1:]):
        delta.append(current - previous)
    return delta


def find_previous(list):
    rows = [list]
    while True:
        delta = create_delta(rows[-1])
        rows.append(delta)
        if all_zero(delta):
            break

    value = 0
    for i, row in enumerate(reversed(rows)):
        if i == 0:
            continue
        value = row[0] - value
    return value


total = 0
for line in lines:
    numbers = [int(x) for x in line.split()]
    total += find_previous(numbers)
print(total)