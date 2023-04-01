from __future__ import annotations
import copy
from typing import Optional, Dict, Iterable, List, Tuple

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

    def __init__(self, color: Player, stones: Iterable[Point]):
        self.color = color
        self.stones = frozenset(stones)

    def merged_with(self, hex_string: HexString) -> HexString:
        assert hex_string.color == self.color
        combined_stones = self.stones | hex_string.stones
        return HexString(self.color, combined_stones)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, HexString) and \
            self.color == other.color and self.stones == other.stones


class Board():
    """A board for the game of Hex."""

    def __init__(self, n: int):
        self.n = n
        self._grid: Dict[Point, HexString] = {}
    
    def is_on_grid(self, point: Point) -> bool:
        """Returns True if the point is on the board."""
        return 1 <= point.r <= self.n and 1 <= point.q <= self.n
    
    def get(self, point: Point) -> Optional[Player]:
        """Returns the content of a point on the board."""
        string = self._grid.get(point)
        if string is None:
            return None
        return string.color

    def get_hex_string(self, point: Point) -> Optional[HexString]:
        """Returns the hex string at a point on the board, or None if the point is empty."""
        return self._grid.get(point)

    def get_all_strings(self) -> List[HexString]:
        """Returns a list of all hex strings on the board."""
        return list(self._grid.values())

    def place_stone(self, player: Player, point: Point) -> HexString:
        assert self.is_on_grid(point)
        assert self._grid.get(point) is None # Make sure point is unoccupied.
        adjacent_same_color: List[HexString] = []

        for neighbor in point.neighbors():
            if not self.is_on_grid(neighbor):
                continue
            neighbor_string = self._grid.get(neighbor)
            if neighbor_string and neighbor_string.color == player:
                adjacent_same_color.append(neighbor_string)
        new_string = HexString(player, [point])

        for same_color_string in adjacent_same_color:
            new_string = new_string.merged_with(same_color_string)
        for new_string_point in new_string.stones:
            self._grid[new_string_point] = new_string
        return new_string

class GameState():
    """The state of a game of Hex."""

    def __init__(self, board: Board, next_player: Player, previous: Optional[GameState], move: Optional[Move]):
        self.board = board
        self.next_player = next_player
        self.previous_state = previous
        self.last_move = move

    @property
    def situation(self) -> Tuple[Player, Board]:
        """Returns the current player and board."""
        return (self.next_player, self.board)

    def apply_move(self, move: Move) -> GameState:
        """Returns the new GameState after applying the move."""
        if isinstance(move, Play):
            next_board = copy.deepcopy(self.board)
            next_board.place_stone(self.next_player, move.point)
        elif isinstance(move, Resign):
            next_board = self.board
        else:
            # TODO: Implement swap
            next_board = self.board

        return GameState(next_board, self.next_player.other, self, move)

    @classmethod
    def new_game(cls, n: int) -> GameState:
        """Returns a new GameState for a game of Hex on an n x n board."""
        board = Board(n)
        return GameState(board, Player.black, None, None)
    
    def is_valid_move(self, move: Move) -> bool:
        if self.is_over():
            return False
        if isinstance(move, Swap) or isinstance(move, Resign):
            # TODO: Implement swap
            return True
        return self.board.get(move.point) is None
    
    def is_over(self) -> bool:
        """Returns True if the game is over."""
        if isinstance(self.last_move, Resign):
            return True
        else:
            # Check if either player has a string of stones from one side of the board to the other.
            for hex_string in self.board.get_all_strings():
                if hex_string.color == Player.black:
                    # Black needs to connect from (q, 1) to (q, n)
                    if 1 in {p.q for p in hex_string.stones} and self.board.n in {p.q for p in hex_string.stones}:
                        return True
                else:
                    # White needs to connect from (1, r) to (n, r)
                    if 1 in {p.r for p in hex_string.stones} and self.board.n in {p.r for p in hex_string.stones}:
                        return True
        return False