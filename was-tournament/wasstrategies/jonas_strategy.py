"""Code retrieved from Axelrod rand.py strategy"""

from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D


class Jonas(Player):
    """A player who randomly chooses between cooperating and defecting.
    This strategy came 15th in Axelrod's original tournament.
    Names:
    - Random: [Axelrod1980]_
    - Lunatic: [Tzafestas2000]_
    """

    name = "Jonas - Strategy1"
    classifier = {
        "memory_depth": 0,  # Memory-one Four-Vector = (p, p, p, p)
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
        self.lost_trust = False
        self.gained_trust = False

    def strategy(self, opponent: Player) -> Action:
        """Actual strategy definition that determines player's action."""
        if len(self.history) == 0:
            return C
        if len(self.history) >= 8:
            if self.gained_trust == False:
                return D
            else:
                return C
        # if opponent history includes a C after a D, then cooperate
        if (
            len(opponent.history) > 1
            and opponent.history[-1] == C
            and opponent.history[-2] == D
        ):
            self.gained_trust = True
            return C
        # if previous round of opponent was a defection, perform defection
        if len(opponent.history) > 0 and opponent.history[-1] == D:
            return D
        # Defect in any other case
        return D

    def _post_init(self):
        super()._post_init()
        if self.p in [0, 1]:
            self.classifier["stochastic"] = False
        # Avoid calls to _random, if strategy is deterministic
        # by overwriting the strategy function.
        if self.p <= 0:
            self.strategy = self.defect
        if self.p >= 1:
            self.strategy = self.cooperate

    @classmethod
    def cooperate(cls, opponent: Player) -> Action:
        return C

    @classmethod
    def defect(cls, opponent: Player) -> Action:
        return D
