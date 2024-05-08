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

    def strategy(self, opponent: Player) -> Action:
        """Actual strategy definition that determines player's action."""
        
        self.round += 1

        """In the first round, the player always cooperates"""
        """Then the player alternates between cooperating and defecting
        starting with at the next round. The alternation becomes slower
        as is will happen at an increasing delay"""
        
        if self.round == 1:
          return C
        elif self.round == 2:
          return D
        elif self.round == 3:
          return C
        elif self.round == 4:
          return C
        elif self.round == 5:
          return D
        elif self.round == 6:
          return D
        elif self.round == 7:
          return C
        elif self.round == 8:
          return C
        elif self.round == 9:
          return C
        else:
          return D