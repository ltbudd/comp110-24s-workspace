"""This is a docstring."""


from __future__ import annotations


__author__ = "730648114"


class Point:
    """This is also a docstring."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float) -> None:
        """Guess what this is."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """And also this."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """And this as well."""
        self.x = self.x * factor
        self.y = self.y * factor
        return self