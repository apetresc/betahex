from __future__ import annotations
from typing import Optional, Dict, Iterable, List, Set, Tuple

from .hextypes import Player, Point

class Play():
    """A move in the game of Hex."""
    
    def __init__(self, point: Point):
        self.point = point

class Resign():
    pass

class Swap():
    pass

Move = Play | Resign | Swap

class HexString():
    """A string of connected stones of the same color."""

    def __init__(self, color: Player, stones: Iterable[Point], liberties: Iterable[Point]):
        self.color = color
        self.stones = frozenset(stones)

    def merged_with(self, hex_string: HexString) -> HexString:
        assert hex_string.color == self.color
        combined_stones = self.stones | hex_string.stones
        return HexString(self.color, combined_stones)

    def __eq__(self, other: HexString) -> bool:
        return self.color == other.color and self.stones == other.stones


class Board():
    """A board for the game of Hex."""

    def __init__(self, n: int):
        self.n = n
        self._grid: Dict[Point, Optional[HexString]] = {}