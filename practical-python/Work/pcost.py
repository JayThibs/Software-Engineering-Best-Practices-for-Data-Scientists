import sys
from pathlib import Path


def portfolio_cost(filepath: str) -> int:
    """
    Calculates the total cost of a stock portfolio.

    Args:
        filepath (str): The filepath to the CSV file containing the stock portfolio.
    Returns:
        total_cost (float): Returns the total cost of the stock portfolio.
    """
    total_cost = 0
    with open(filepath, "rt") as f:
        headers = next(f)
        for line in f:
            row = line.split(",")
            share = int(row[1])
            price = float(row[2])
            total_cost += share * price

        return total_cost


if len(sys.argv) == 2:
    filepath = sys.argv[1]
else:
    filepath = str(Path(".").resolve() / "practical-python/Work/Data/portfolio.csv")

cost = portfolio_cost(filepath)
print(f"Total cost: {cost:0.2f}")
