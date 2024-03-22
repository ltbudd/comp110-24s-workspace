"""Some functions for my garden plan!"""

__author__ = "730648114"

def add_by_kind(pbook: dict[str, list[str]], pkey: str, padd: str) -> None:
    """Mutates dictionary using input strings."""
    pbook[pkey].append(padd)

def add_by_date(dbook: dict[str, list[str]], dkey: str, dadd: str) -> None:
    """Mutates dictionary using input strings."""
    dbook[dkey].append(dadd)

def lookup_by_kind_and_date(pbook: dict[str, list[str]], dbook: dict [str, list[str]], pkey: str, dkey: str) -> str:
    """Returns string of which plants to plant in a given month."""
    dlist: list = (dbook[dkey])
    plist: list = (pbook[pkey])
    thing: list = list()
    if len(dlist) > len(plist):
        for i in plist:
            if i in dlist:
                thing.append(i)
    else:
        for i in dlist:
            if i in plist:
                thing.append(i)
    if len(thing) == 0:
        print(f"No flowers to plant in {dkey}")
    else:
        print(f"flowers to plant in {dkey}: {thing}.")