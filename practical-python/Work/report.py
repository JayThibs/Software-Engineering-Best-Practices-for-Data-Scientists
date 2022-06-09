import os
import csv
import sys
from pathlib import Path
from pprint import pprint


def read_portfolio(filename: str):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(holding)
    return portfolio


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
        
def read_prices(filename: str) -> dict:
    """Reads a set of prices and puts them into a dictionary."""
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        try:
            for row in rows:
                prices[str(row[0])] = float(row[1])
        except IndexError:
            pass
    return prices

portfolio = read_portfolio('Data/portfolio.csv') # current personal portfolio
prices    = read_prices('Data/prices.csv') # current prices in stock market

# Calculate total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s["shares"] * s["price"]

# Calculate the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += s["shares"] * prices[s["name"]]

print("Current value:", total_value)
print("Gain:", total_value - total_cost)