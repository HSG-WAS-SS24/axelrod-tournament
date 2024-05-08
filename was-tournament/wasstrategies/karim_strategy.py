"""Code retrieved from Axelrod rand.py strategy"""
from random import random

from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D


class Karim(Player):
    """A player who randomly chooses between cooperating and defecting.
    This strategy came 15th in Axelrod's original tournament.
    Names:
    - Random: [Axelrod1980]_
    - Lunatic: [Tzafestas2000]_
    """

    name = "Karim - Simple"
    classifier = {
        "memory_depth": 0,
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
        if len(opponent.history) == 0:
            return C
        if opponent.history[-1] == C:
            return C
        if opponent.history[-1] == D:
            return D


class Karim2(Player):
    """A player who randomly chooses between cooperating and defecting.
    This strategy came 15th in Axelrod's original tournament.
    Names:
    - Random: [Axelrod1980]_
    - Lunatic: [Tzafestas2000]_
    """

    name = "Karim - Ressurection"
    classifier = {
        "memory_depth": 0,
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
        if len(self.history) == 0:
            return C
        if len(self.history) >= 5 and self.history[-5:] == [D, D, D, D, D]:
            return D
        else:
            return opponent.history[-1]



