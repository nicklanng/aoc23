with open('input') as f:
    lines = [line.rstrip() for line in f]

class SeedRange:
    def __init__(self, start, r):
        self.start = start
        self.range = r
    
    def contains(self, input):
        return input >= self.start and input < self.start + self.range


class Category:
    def __init__(self):
        self.ranges = []

    def add_range(self, range):
        self.ranges.append(range)
    
    def process(self, input):
        for range in self.ranges:
            if range.contains(input):
                return range.process(input)
        return input


class Range:
    def __init__(self, dst_start, src_start, r):
        self.dst_start = dst_start
        self.src_start = src_start
        self.range = r
    
    def contains(self, input):
        return input >= self.dst_start and input < self.dst_start + self.range
    
    def process(self, input):
        d = input - self.dst_start
        return self.src_start + d


seedRanges = []
categories = {
    "seed-to-soil": Category(),
    "soil-to-fertilizer": Category(),
    "fertilizer-to-water": Category(),
    "water-to-light": Category(),
    "light-to-temperature": Category(),
    "temperature-to-humidity": Category(),
    "humidity-to-location": Category(),
}

def parse_file(lines):
    for i in range(0, len(lines)):
        if i == 0:
            seedTokens = [int(x) for x in lines[i].removeprefix("seeds: ").split()]
            for j in range(int(len(seedTokens)/2)):
                seedRanges.append(SeedRange(seedTokens[j*2], seedTokens[j*2+1]))
            continue

        if "map:" in lines[i]:
            token = lines[i].split()
            category = categories[token[0]]
            i += 1
            while len(lines[i]) > 0:
                tokens = lines[i].split()
                category.add_range(Range(int(tokens[0]), int(tokens[1]), int(tokens[2])))
                i += 1
                if i >= len(lines):
                    return


def run_search():
    i = 0
    while True:
        i += 1
        if i % 100000 == 0:
            print("working: ", i)
        result = categories["humidity-to-location"].process(i)
        result = categories["temperature-to-humidity"].process(result)
        result = categories["light-to-temperature"].process(result)
        result = categories["water-to-light"].process(result)
        result = categories["fertilizer-to-water"].process(result)
        result = categories["soil-to-fertilizer"].process(result)
        result = categories["seed-to-soil"].process(result)
        for seedRange in seedRanges:
            if seedRange.contains(result): 
                print(i)
                return
      
parse_file(lines)      
run_search()