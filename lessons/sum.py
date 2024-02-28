"""Summing the elements of a list using different loops."""

__author__ = "730648114"

# Defining w_sum function
def w_sum(vals: list[float]) -> float:
    i = 0
    result: float = 0.0
    while i < len(vals):
        result += vals[i]
        i += 1
    return result

# Defining f_sum function
def f_sum(vals: list[float]) -> float:
    result: float = 0.0
    for i in vals:
        result += i
    return result

# Defining f_range_sum function
def f_range_sum(vals: list[float]) -> float:
    result: float = 0.0
    for i in range(len(vals)):
        result += vals[i]
    return result