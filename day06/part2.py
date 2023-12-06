import math

with open('input') as f:
    lines = [line.rstrip() for line in f]

    
time = int(lines[0].removeprefix("Time: ").replace(" ", ""))
distance = int(lines[1].removeprefix("Distance: ").replace(" ", ""))

total_ways = 0
for t in range(time):
    speed = t
    remaining_time = time-t
    d = speed*remaining_time
    if d > distance:
        total_ways += 1
print(total_ways)