from __future__ import annotations
import enum
from typing import List, NamedTuple

class Player(enum.Enum):
    """A player in a game of Hex."""
    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white
    

class Point(NamedTuple):
    r: int
    q: int
    """A point on a hexagonal board, using the axial coordinate system.
    
    The details of this coordinate system are described in the following
    article: https://www.redblobgames.com/grids/hexagons/#coordinates
    """

    def neighbors(self) -> List[Point]:
       """Returns all neighboring points on the hex grid."""
       return [
            Point(self.r    , self.q - 1),
            Point(self.r + 1, self.q - 1),
            Point(self.r + 1, self.q    ),
            Point(self.r    , self.q + 1),
            Point(self.r - 1, self.q + 1),
            Point(self.r - 1, self.q    )
       ]