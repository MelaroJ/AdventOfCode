# AOC Day 1
# https://adventofcode.com/2024/day/1

import pathlib
import polars as pl
import polars.selectors as cs
import time

input_path = pathlib.Path("2024/01.in")

start_time = time.time()

distance = (
        pl.scan_csv(
            input_path,
            has_header = False,
            separator = "\t"
        )
        .with_columns(
            ids = 
            cs.first()
            .str.extract_groups(r"(?<id1>\d+)\s+(?<id2>\d+)")
            )
        .with_columns(
            id1 = pl.col("ids").struct["id1"].sort()
            )
        .with_columns(
            id2 = pl.col("ids").struct["id2"].sort()
            )
        .select(cs.matches("id[0-9]"))
        .with_columns(
            dist = pl.Expr.abs(pl.col("id2").cast(pl.Int32) - pl.col("id1").cast(pl.Int32))
            )
        .select(cs.last())
        .collect()
    ).sum().item()

ids = (
    pl.scan_csv(
        input_path,
        has_header=False,
        separator="\t"
    )
    .with_columns(
        ids=cs.first()
        .str.extract_groups(r"(?<id1>\d+)\s+(?<id2>\d+)")
    )
    .with_columns(
        id1=pl.col("ids").struct["id1"].sort()
    )
    .with_columns(
        id2=pl.col("ids").struct["id2"].sort()
    )
    .select(cs.matches("id[0-9]"))
    .collect()
)

id1 = (
    ids
    .select(pl.col("id1"))
    .to_series().to_list()
    )

sim_score = (
    ids
    .select(pl.col("id2").value_counts(sort=True))
    .unnest("id2")
    .filter(pl.col("id2").is_in(id1))
    .with_columns(
        score = pl.col("id2").cast(pl.UInt32) * pl.col("count")
        )
    .select(pl.col("score"))
).sum().item()



end_time = time.time()

print(f"p1: \n{distance}")
print(f"p2: \n{sim_score}")
print(f"Elapsed time: {(end_time - start_time):.3f} seconds")

