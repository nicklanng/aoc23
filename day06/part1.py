import math

with open('input') as f:
    lines = [line.rstrip() for line in f]

    
times = [int(x) for x in lines[0].removeprefix("Time: ").split()]
distances = [int(x) for x in lines[1].removeprefix("Distance: ").split()]

totals = []
for i, time in enumerate(times):
    total_ways = 0
    for t in range(time):
        speed = t
        remaining_time = time-t
        distance = speed*remaining_time
        if distance > distances[i]:
            total_ways += 1
    totals.append(total_ways)

print(math.prod(totals))