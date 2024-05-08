"""Code retrieved from Axelrod rand.py strategy"""

from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D


class David(Player):
    """A player who randomly chooses between cooperating and defecting.
    This strategy came 15th in Axelrod's original tournament.
    Names:
    - Random: [Axelrod1980]_
    - Lunatic: [Tzafestas2000]_
    """

    count = 0;
    name = "David - Kobayashi Maru"
    classifier = {
        "memory_depth": 0,   # Memory-one Four-Vector = (p, p, p, p)
        "stochastic": True,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def __init__(self, p: float = 0.5) -> None:
        """
        Parameters
        ----------
        p, float
            The probability to cooperate
        Special Cases
        -------------
        Random(0) is equivalent to Defector
        Random(1) is equivalent to Cooperator
        """
        super().__init__()
        self.p = p

    def strategy(self, opponent: Player) -> Action:
        """Actual strategy definition that determines player's action."""
        self.count += 1
        if self.count % 4 == 0:
            return self.cooperate(opponent)
        else:
            return self.defect(opponent)

    @classmethod
    def cooperate(cls, opponent: Player) -> Action:
        return C

    @classmethod
    def defect(cls, opponent: Player) -> Action:
        return D