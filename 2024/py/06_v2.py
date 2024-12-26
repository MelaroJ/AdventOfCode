import time

start = time.time()

grid = list(map(list, open('2024/06.in').read().splitlines()))

rows = len(grid)
cols = len(grid[0])

# Find the initial position of the '^' symbol
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "^":
            break
    else:
        continue
    break

def traverse(grid, r, c):
    """Perform traversal starting from (r, c) and return the p1 set."""
    dr, dc = -1, 0
    seen = set()

    while True:
        seen.add((r, c))
        if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
            break
        if grid[r + dr][c + dc] == "#":
            dc, dr = -dr, dc  # Rotate direction
        else:
            r += dr
            c += dc

    return seen

def count_loops(grid, p1):
    """Count the number of loops formed by placing walls ('#') in empty cells ('.')."""
    def loops(grid, r, c):
        dr, dc = -1, 0
        seen = set()

        while True:
            seen.add((r, c, dr, dc))
            if r + dr < 0 or r + dr >= rows or c + dc < 0 or c + dc >= cols:
                return False
            if grid[r + dr][c + dc] == "#":
                dc, dr = -dr, dc  # Rotate direction
            else:
                r += dr
                c += dc
            if (r, c, dr, dc) in seen:
                return True

    count = 0
    for cr, cc in p1:
        if grid[cr][cc] != ".":
            continue
        grid[cr][cc] = "#"  # Temporarily place a wall
        if loops(grid, r, c):
            count += 1
        grid[cr][cc] = "."  # Restore the original cell

    return count

# Part 1: Traverse and collect visited cells
p1 = traverse(grid, r, c)

# Part 2: Use the p1 cells to speed up loop detection
p2 = count_loops(grid, p1)

# Outputs
print(f"p1: \n{len(p1)}")
print(f"p2: \n{p2}")
print(f"Time elapsed: {(time.time()-start):.3f} seconds")
