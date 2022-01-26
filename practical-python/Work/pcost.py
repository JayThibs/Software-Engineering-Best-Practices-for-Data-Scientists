from pathlib import Path

filepath = str(Path(".").resolve() / "practical-python/Work/Data/portfolio.csv")
total_cost = 0

with open(filepath, "rt") as f:
    headers = next(f)
    for line in f:
        row = line.split(",")
        share = int(row[1])
        price = float(row[2])
        total_cost += share * price

print(f"Total cost: {total_cost:0.2f}")
