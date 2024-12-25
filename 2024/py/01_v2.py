# AOC Day 1
# https://adventofcode.com/2024/day/1

import time

a = list(map(list, zip(*[list(map(int, line.split()))
                   for line in open('2024/01.in').read().splitlines()]
             )
         )
     )

l, r = a

start = time.time()

for k in a: k.sort()

print(f"pt 1: \n{sum(abs(x - y) for x, y in zip(*a))}")
print(f"pt 2: \n{sum(x * r.count(x) for x in l)}")
print(f"Elapsed time: {( time.time() - start ):.3f} seconds")
