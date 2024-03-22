"""Splitting a dictionary into two lists."""


__author__ = "730648114"


# Defining get_keys function


def get_keys(book: dict[str, int]) -> list[str]:
    """"Signature."""
    kbook: list[str] = list()
    for key in book:
        kbook.append(key)
    return kbook


# Defining get_values function


def get_values(book: dict[str, int]) -> list[int]:
    """Signature."""
    kbook: list[int] = list()
    for key in book:
        kbook.append(book[key])
    return kbook