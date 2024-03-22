"""Dictionary Function Exercise."""


__author__ = "730648114"


def invert(din: dict[str, str]) -> dict[str, str]:
    """Keys of input list become values of output list, and vice versa."""
    rev: dict[str, str] = dict()
    for i in din:
        if din[i] in rev:
            raise KeyError("KeyError")
        else:
            rev[din[i]] = i
    return rev


def favorite_color(din: dict[str, str]) -> str:
    """Returns most popular color from input."""
    book: dict[str, int] = dict()
    for i in din:
        if din[i] in book:
            book[din[i]] += 1
        else:
            book[din[i]] = 1
    print(book)
    count: int = 0
    color: str = ""
    for i in book:
        if book[i] > count:
            count = book[i]
            color = i
    return color


def count(lin: list[str]) -> dict[str, int]:
    """Each key is a list value, and each value is the # of times that key appeared in the list."""
    book: dict[str, int] = dict()
    for i in lin:
        if i in book:
            book[i] += 1
        else:
            book[i] = 1
    return(book)


def alphabetizer(lin: list[str]) -> dict[str, list[str]]:
    """Placeholder!"""
    book: dict[str, list[str]] = dict()
    for i in lin:
        if i[0].isalpha():
            letter = i[0].lower()
            if letter not in book:
                book[letter] = []
            book[letter].append(i)
    return book


def update_attendance(din: dict[str, list[str]], day: str, name: str) -> None:
    """Placeholder!"""
    if day in din:
        din[day].append(name)
    else:
        din[day] = [name]
    return None