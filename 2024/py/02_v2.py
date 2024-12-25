# AOC Day 2
# https://adventofcode.com/2024/day/2

import time

start = time.time()

p1_count = 0
p2_count = 0

def safe(levels):
    diffs = [x - y for x, y in zip(levels, levels[1:])]
    return all(1 <= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs)

for report in open('2024/02.in'):
    levels = list(map(int, report.split()))
    if safe(levels):
        p1_count += 1

for report in open('2024/02.in'):
    levels = list(map(int, report.split()))
    if any(safe(levels[:index] + levels[index + 1:]) for index in range(len(levels))):
        p2_count += 1

end = time.time()

print(f"p1: \n{p1_count}")
print(f"p2: \n{p2_count}")
print(f"Time elapsed: {(end-start):.3f} seconds")


