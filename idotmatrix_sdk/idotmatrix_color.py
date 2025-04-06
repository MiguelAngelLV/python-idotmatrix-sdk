"""An IDotMatrix color module."""
# pylint: disable=W0246

from dataclasses import dataclass
from random import randint


@dataclass
class IDotMatrixColor:
    """Class representing a color for the IDotMatrix."""

    red: int
    green: int
    blue: int

    @staticmethod
    def random_color():
        """Generate a random color."""
        return IDotMatrixColor(randint(0, 255), randint(0, 255), randint(0, 255))
