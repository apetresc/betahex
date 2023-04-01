from dlhex.agent import naive
from dlhex.hexboard import GameState
from dlhex.hextypes import Player
from dlhex.utils import print_diamond_board, print_move

import time


def main():
    board_size = 13
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
        time.sleep(0.3)


if __name__ == '__main__':
    main()