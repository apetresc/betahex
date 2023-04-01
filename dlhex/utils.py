from rich import print
from typing import List

from .hextypes import Player, Point
from .hexboard import Board, Move, Play, Resign

COLS = 'ABCDEFGHJKLMNOPQRST'
STONE_TO_CHAR = {
    None: '[dim yellow]·[/dim yellow]',
    Player.black: '[bold black]#[/bold black]',
    Player.white: '[bold white]O[/bold white]'
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
    return f'{COLS[point.r - 1]}{point.q}'

def point_from_coords(coords: str) -> Point:
    """Converts a two-character string, like 'B3', to a point."""
    col = COLS.index(coords[0].upper()) + 1
    row = int(coords[1:])
    return Point(col, row)

def print_board(board: Board) -> None:
    """Prints the board."""
    for row in range(board.n, 0, -1):
        bump = ' ' if row % 2 == 0 else ''
        line: List[str] = []
        for col in range(1, board.n + 1):
            stone = board.get(Point(row, col))
            line.append(STONE_TO_CHAR[stone])
        print(f'{row:02}{bump} {" ".join(line)}')

def print_diamond_board(board: Board) -> None:
    """Prints the board in a diamond (rather than rectangular) configuration."""

    print('   ' * (board.n - 1) + f' {COLS[board.n - 1]}     1')
    for row in range(board.n, 0, -1):
        bump = '   ' * (row - 2) + f' {COLS[row - 2]}   ' if row > 1 else '  '
        print(bump, end='')
        for r, q in zip(range(row, board.n + 1), range(1, board.n + 1)):
            stone = board.get(Point(r, q))
            print(f'  {STONE_TO_CHAR[stone]}   ', end='')
        if row > 1:
            print(f' {board.n - row + 2:2}', end="")
        print()
    
    for row in range(2, board.n + 1):
        bump = '   ' * (row - 2) + f'{row - 1:2}   '
        print(bump, end='')
        for r, q in zip(range(1, board.n + 1), range(row, board.n + 1)):
            stone = board.get(Point(r, q))
            print(f'  {STONE_TO_CHAR[stone]}   ', end='')
        # Print right axis labels
        print(f'  {COLS[board.n - row + 1]}')
    print('   ' * (board.n - 1) + f'{board.n:2}     A')