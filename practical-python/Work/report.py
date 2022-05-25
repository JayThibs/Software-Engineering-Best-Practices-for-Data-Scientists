import csv
import sys
from pathlib import Path


def read_portfolio(filename: str):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return print(portfolio)


def portfolio_cost(filename: str) -> float:
    """Computes the total cost (shares*price) of a portfolio file."""
    total_cost = 0.0

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost
        


if len(sys.argv) == 2:
    filepath = sys.argv[1]
else:
    filepath = str(Path(".").resolve() / "practical-python/Work/Data/portfolio.csv")

read_portfolio(filepath)
