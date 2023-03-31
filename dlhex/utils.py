from typing import List

from .hextypes import Player, Point
from .hexboard import Board, Move, Play, Resign

COLS = 'ABCDEFGHJKLMNOPQRST'
STONE_TO_CHAR = {
    None: '.',
    Player.black: '#',
    Player.white: 'O'
}

def print_move(player: Player, move: Move):
    """Prints the move for the player."""
    if isinstance(move, Play):
        print(f'{player} plays {point_to_coords(move.point)}')
    elif isinstance(move, Resign):
        print(f'{player} resigns')
    else:
        print(f'{player} swaps')

def point_to_coords(point: Point) -> str:
    """Converts a point to a two-character string, like 'B3'."""
    return f'{COLS[point.q - 1]}{point.r}'

def print_board(board: Board) -> None:
    """Prints the board."""
    for row in range(board.n, 0, -1):
        bump = ' ' if row % 2 == 0 else ''
        line: List[str] = []
        for col in range(1, board.n + 1):
            stone = board.get(Point(row, col))
            line.append(STONE_TO_CHAR[stone])
        print(f'{row:02}{bump} {" ".join(line)}')