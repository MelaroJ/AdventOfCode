import re
import time

start = time.time()

memory = open("2024/03.in").read()

p1_count = 0

for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory):
    x, y = map(int, match[4:-1].split(","))
    p1_count += x * y

on = True
p2_count = 0

for match in re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", memory):
    if match == "do()":
        on = True
    elif match == "don't()":
        on = False
    elif on:
        x, y = map(int, match[4:-1].split(","))
        p2_count += x * y

print(f"p1: \n{p1_count}")
print(f"p2: \n{p2_count}")
print(f"Time elapsed: {(time.time()-start):.3f} seconds")
