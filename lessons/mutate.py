"""Mutating functions."""

__author__ = "730648114"

def manual_append(a: list[int], num: int) -> None:
    b: list[int] = a
    a.append(num)

def double(a: list[int]) -> None:
    i = 0
    while i < len(a):
        a[i] = a[i] * 2
        i += 1