import polars as pl
import time

input_path = "2024/03.in"

start = time.time()

p1 = (
    (
    pl.scan_csv(
       input_path,
       has_header = False,
       separator = "\n",
       new_columns = ["memory"],
        )
    .select(
        pl.col("memory")
        .str.join()
        .str.extract_all(
            r"mul\(\d+,\d+\)"   
            )
        .explode()
        .str.extract_groups(
                r"(?<m1>\d+),(?<m2>\d+)"
            )
        )
    .unnest("memory")
    .with_columns(
        (pl.col("m1").cast(pl.UInt32) * pl.col("m2").cast(pl.UInt32)) 
        .alias("prod")
        )
    .select(
       pl.selectors.last()
       )
    )
    .collect()
    .sum()
    .item()
)

memory = (
(
pl.scan_csv(
   input_path,
   has_header = False,
   separator = "\n",
   new_columns = ["memory"],
    )
.select(
    pl.col("memory")
    .str.join()
    .str.extract_all(
        r"mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)"   
        )
    .explode()
   )
)
.collect()
.to_series()
.to_list()
)

p2 = []

keep_values = True
for keywords in memory:
    if keywords == "don't()":
        keep_values = False
        pass
    if keywords == "do()":
        keep_values = True
    if keep_values and keywords != "do()":
        p2.append(keywords)

p2 = (
    (
    pl.DataFrame(
        {
            "memory": p2
        }
    )
    .select(
        pl.col("memory")
        .str.extract_groups(
           r"(?<m1>\d+),(?<m2>\d+)"
            )
        )
    .unnest("memory")
    .with_columns(
        (pl.col("m1").cast(pl.UInt32) * pl.col("m2").cast(pl.UInt32))
        .alias("prod")
        )
    .select(
        pl.col("prod")
        )
    )
    .sum()
    .item()
)


end = time.time()

print(f"p1: \n{p1}")
print(f"p2: \n{p2}")
print(f"Time elapsed: {(end-start):.3f} seconds")
