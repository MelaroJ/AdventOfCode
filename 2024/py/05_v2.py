import functools
import time

start = time.time()

file = open('2024/05.in')

rules = []
for line in file:
    if line.isspace(): break
    rules.append(list(map(int, line.split("|"))))

cache_p1 = {}
cache_p2 = {}

for x, y in rules:
    cache_p1[(x, y)] = True
    cache_p1[(y, x)] = False
    cache_p2[(x, y)] = -1
    cache_p2[(y, x)] = 1

def is_ordered_p1(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            key = (update[i], update[j])
            if key in cache_p1 and not cache_p1[key]:
                return False
    return True

def is_ordered_p2(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            key = (update[i], update[j])
            if key in cache_p2 and cache_p2[key] == 1:
                return False
    return True

def cmp(x, y):
    return cache_p2.get((x, y), 0)

# reset file pointer
for _ in range(len(rules) + 1):  # Skip rules and blank line
    next(file)

p1_count = 0
p2_count = 0

for line in file:
    update = list(map(int, line.split(",")))

    if is_ordered_p1(update):
        p1_count += update[len(update) // 2]

    if not is_ordered_p2(update):
        update.sort(key=functools.cmp_to_key(cmp))
        p2_count += update[len(update) // 2]

print(f"p1: \n{p1_count}")
print(f"p2: \n{p2_count}")
print(f"Time elapsed: {(time.time()-start):.3f} seconds")
