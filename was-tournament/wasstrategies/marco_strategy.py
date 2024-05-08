from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D


class Marco(Player):
    """A player who chooses between cooperating and defecting in an alternating fashion, however, with increasing step."""

    name = "Marco - IncreasingAlternator"
    classifier = {
        "memory_depth": 0,   # Memory-one Four-Vector = (p, p, p, p)
        "stochastic": True,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self) -> None:
        super().__init__()
        self.round = 0
        self.choices = [C, D, C, C, D, D, C, C, C, D]

    def strategy(self, opponent: Player) -> Action:
        """Actual strategy definition that determines player's action."""
        
        choice = self.choices[self.round]
        self.round += 1

        return choice