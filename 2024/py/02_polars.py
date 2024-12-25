# AOC Day 2
# https://adventofcode.com/2024/day/2

import polars as pl
import time
from itertools import combinations

# Function to check if a report is valid
# 1) adjacent levels must be ALL be increasing/decreasing (i.e., monotonic, can't have both)
# 2) absolute value of adjacent level diffs must be between 1-3 inclusive
def is_valid(report):
    # Generate all modified reports (remove one level at a time)
    modified_reports = [list(comb) for comb in combinations(report, len(report) - 1)]
    
    for modified in modified_reports:
        # Compute differences between adjacent levels
        diffs = [modified[i + 1] - modified[i] for i in range(len(modified) - 1)]
        
        # Check monotonicity
        monotonic = all(x >= 0 for x in diffs) or all(x <= 0 for x in diffs)
        # Check difference range
        valid_diff = all(1 <= abs(x) <= 3 for x in diffs)
        
        # If both criteria are met, return True
        if monotonic and valid_diff:
            return True
    
    # If no modified report satisfies the criteria, return False
    return False

start = time.time()

# Path to input txt
input_path = "02.in"

# Lazily read file and process it
p1_count = (
    pl.scan_csv(
        input_path,
        has_header=False,
        separator="\n",    # Treat each report as single row
        new_columns=["report"]  # Column holding raw lines
    )
   # Split lines into lists of strings
    .with_columns(
        report=pl.col("report")
        .str.split(" ")
    )
    # lists of strings -> lists of ints
    .with_columns(
        pl.col("report")
        .list.eval(
            pl.element()
            .cast(pl.Int64)
        )
        .alias("report")
    )
    # Compute diff between adjacent levels in reports
    .with_columns(
        pl.col("report")
        .list.eval(
            pl.element()
            .diff(null_behavior="drop")
        )
        .alias("diff")
    )
    # Determine safe rows
    .with_columns(
        pl.col("diff")
        .list.eval(
            (pl.element().abs() >= 1) & (pl.element().abs() <= 3)
            &
            (
                (pl.element().sign().min() > 0) & (pl.element().sign().max() > 0)
                | (pl.element().sign().min() < 0) & (pl.element().sign().max() < 0)
            )
        )
        .alias("safe")
        .list
        .all()
    )
    # Select safe column, sum rows, collect and extract 
    .select(pl.col("safe"))
    .sum()
    .collect()
    .item()
)

df = (
    pl.scan_csv(
        input_path,
        has_header=False,
        separator="\n",    # Treat each report as single row
        new_columns=["report"]  # Column holding raw lines
    )
   # Split lines into lists of strings
    .with_columns(
        pl.col("report")
        .str.split(" ")
    )
    # lists of strings -> lists of ints
    .with_columns(
        pl.col("report")
       .list.eval(
            pl.element().cast(pl.Int64)
        )
    )
).collect()

# Apply the validation function to each report
p2_count = (
    df.with_columns(
        pl.col("report")
            .map_elements(
                is_valid,
                return_dtype=pl.Boolean()
            )
            .alias("valid")
    )
    .select(pl.col("valid"))
    .sum()
    .item()
)

end = time.time()

print(f"p1: \n{p1_count}")
print(f"p2: \n{p2_count}")
print(f"Time elapsed: {(end-start):.3f} seconds")

