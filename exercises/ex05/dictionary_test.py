"""Dictionary test stuff."""

__author__ = "730648114"

from dictionary import invert, alphabetizer, favorite_color, count, update_attendance

# - - - - - - - - - - - - - - - - - - - - #
def test_invert_int() -> None:
    """Invert should work with integers."""
    test: dict[int, int] = {1:5, 2:10, 3:15, 4:20}
    assert invert(test) == {5:1, 10:2, 15:3, 20:4}

def test_invert_str() -> None:
    """Invert should work with strings."""
    test: dict[str, str] = {"ab":"ba", "cd":"dc", "yz":"zy"}
    assert invert(test) == {"ba":"ab", "dc":"cd", "zy":"yz"}

def test_invert_edge() -> None:
    """Invert should raise KeyError when encountering duplicate keys."""
    test: dict[bool, int] = {True:1, False:2, True:3, True:4}
    assert invert(test) == {1:True, 2:False, 3:True, 4:True}

# - - - - - - - - - - - - - - - - - - - - #
def test_alphabetizer_

# - - - - - - - - - - - - - - - - - - - - #


# - - - - - - - - - - - - - - - - - - - - #


# - - - - - - - - - - - - - - - - - - - - #