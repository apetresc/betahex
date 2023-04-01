from ..hexboard import GameState, Move

class Agent():
    """Abstract base class for an agent to play Hex."""
    def __init__(self):
        pass

    def select_move(self, game_state: GameState) -> Move:
        """Selects a move for the agent to play."""
        raise NotImplementedError()

