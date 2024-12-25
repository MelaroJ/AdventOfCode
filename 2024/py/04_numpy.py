import time
import numpy as np

start = time.time()

# Load the grid into a NumPy array
grid = np.array([list(row) for row in open('2024/04.in').read().splitlines()])
rows, cols = grid.shape

# Part 1 Optimization
p1_count = 0
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for dr, dc in directions:
    # Compute valid indices within bounds for 3 steps in the given direction
    r_start = max(0, -3 * dr)
    r_end = min(rows, rows - 3 * dr)
    c_start = max(0, -3 * dc)
    c_end = min(cols, cols - 3 * dc)

    # Extract sub-grids and compare sequential characters
    x_mask = (grid[r_start:r_end, c_start:c_end] == "X")
    m_mask = (grid[r_start + dr:r_end + dr, c_start + dc:c_end + dc] == "M")
    a_mask = (grid[r_start + 2 * dr:r_end + 2 * dr, c_start + 2 * dc:c_end + 2 * dc] == "A")
    s_mask = (grid[r_start + 3 * dr:r_end + 3 * dr, c_start + 3 * dc:c_end + 3 * dc] == "S")

    p1_count += np.sum(x_mask & m_mask & a_mask & s_mask)

# Part 2 Optimization
p2_count = 0
# Sub-grid offsets for corners
corner_offsets = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

# Create masks for the center "A" and corner characters
a_mask = (grid[1:-1, 1:-1] == "A")
corners = [
    grid[1 + r_offset:rows - 1 + r_offset, 1 + c_offset:cols - 1 + c_offset]
    for r_offset, c_offset in corner_offsets
]

# Concatenate corner strings and compare to valid patterns
corner_combinations = np.char.add(np.char.add(corners[0], corners[1]), np.char.add(corners[2], corners[3]))
patterns = {"MMSS", "MSSM", "SSMM", "SMMS"}

# Count matches
p2_count = np.sum(np.isin(corner_combinations, list(patterns)) & a_mask)

# Print results
print(f"p1: {p1_count}")
print(f"p2: {p2_count}")
print(f"Time elapsed: {(time.time()-start):.3f} seconds")

