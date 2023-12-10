with open('input') as f:
    lines = [line.rstrip() for line in f]


graph = {}


def get_char(coord):
    return lines[coord[1]][coord[0]]


def find_start():
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'S':
                return (x, y)


def find_connections_incoming(coord):
    up = (coord[0], coord[1]-1)
    down = (coord[0], coord[1]+1)
    left = (coord[0]-1, coord[1])
    right = (coord[0]+1, coord[1])

    up_char = get_char(up)
    down_char = get_char(down)
    left_char = get_char(left)
    right_char = get_char(right)

    connections = []

    if up_char in ['|', '7', 'F']:
        connections.append(up)
    if down_char in ['|', 'L', 'J']:
        connections.append(down)
    if left_char in ['-', 'L', 'F']:
        connections.append(left)
    if right_char in ['-', 'J', '7']:
        connections.append(right)
    
    return connections


def find_connections_outgoing(coord):
    char = get_char(coord)
    match char:
        case '|':
            return [(coord[0], coord[1]-1), (coord[0], coord[1]+1)]
        case '-':
            return [(coord[0]-1, coord[1]), (coord[0]+1, coord[1])]
        case 'L':
            return [(coord[0], coord[1]-1), (coord[0]+1, coord[1])]
        case 'J':
            return [(coord[0], coord[1]-1), (coord[0]-1, coord[1])]
        case '7':
            return [(coord[0], coord[1]+1), (coord[0]-1, coord[1])]
        case 'F':
            return [(coord[0], coord[1]+1), (coord[0]+1, coord[1])]
        case _: return []


# init
open_list = []
start = find_start()
connections = find_connections_incoming(start)
graph[start] = connections
open_list.extend(connections)

# build graph
while len(open_list) > 0:
    open = open_list.pop()
    if open in graph:
        continue
    connections = find_connections_outgoing(open)
    graph[open] = connections
    open_list.extend(connections)

# find furthest point
visited = {start}
highest = (start, 0)
open_list.append(highest)
while len(open_list) > 0:
    open = open_list.pop(0)
    connections = graph[open[0]]
    for connection in connections:
        if connection not in visited:
            if open[1]+1 > highest[1]:
                highest = (connection, open[1]+1)
            open_list.append((connection, open[1]+1))
            visited.add(connection)
print(highest)
