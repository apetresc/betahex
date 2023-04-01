import random
from typing import List

from .base import Agent
from ..hexboard import GameState, Move, Play
from ..hextypes import Point

class RandomBot(Agent):
    def select_move(self, game_state: GameState) -> Move:
        """Selects a random valid move"""
        candidates: List[Move] = []
        for r in range(1, game_state.board.n + 1):
            for q in range(1, game_state.board.n + 1):
                candidate: Move = Play(Point(r=r, q=q))
                if game_state.is_valid_move(candidate):
                    candidates.append(candidate)
        return random.choice(candidates)