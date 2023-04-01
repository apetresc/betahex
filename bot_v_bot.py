import argparse

from dlhex.agent import naive
from dlhex.hexboard import GameState
from dlhex.hextypes import Player
from dlhex.utils import print_diamond_board, print_move


def main(board_size: int = 13):
    game = GameState.new_game(board_size)
    bots = {
        Player.black: naive.RandomBot(),
        Player.white: naive.RandomBot(),
    }

    while not game.is_over():
        bot_move = bots[game.next_player].select_move(game)
        game = game.apply_move(bot_move)
        print_diamond_board(game.board)
        print_move(game.next_player.other, bot_move)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--board-size', '-n', type=int, default=13)
    args = parser.parse_args()

    main(args.board_size)