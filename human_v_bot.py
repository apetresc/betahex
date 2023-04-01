import argparse

from dlhex.hexboard import GameState, Play
from dlhex.hextypes import Player
from dlhex.agent import naive
from dlhex.utils import print_diamond_board, print_move, point_from_coords


def main(board_size: int = 13):
    game = GameState.new_game(board_size)
    bot = naive.RandomBot()
    while not game.is_over():
        print_diamond_board(game.board)
        if game.next_player == Player.black:
            human_move = input('-- ')
            point = point_from_coords(human_move.strip())
            move = Play(point)
        else:
            move = bot.select_move(game)
        print_move(game.next_player, move)
        game = game.apply_move(move)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--board-size', '-n', type=int, default=13)
    args = parser.parse_args() 

    main(args.board_size)