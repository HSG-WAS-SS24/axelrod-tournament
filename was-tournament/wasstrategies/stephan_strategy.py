"""Code retrieved from Axelrod rand.py strategy"""

from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D


class Stephan(Player):
    """A player who randomly chooses between cooperating and defecting.
    This strategy came 15th in Axelrod's original tournament.
    Names:
    - Random: [Axelrod1980]_
    - Lunatic: [Tzafestas2000]_
    """

    name = "Stephan"
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

        self.cooperation_count = 0
        self.is_defecting = True

    def strategy(self, opponent: Player) -> Action:
        if self.is_defecting:

            self.cooperation_count = sum(1 for action in opponent.history if action == C)
            if self.cooperation_count >= 4:
                self.is_defecting = False  
                return C
            return D
        else:

            if opponent.history[-1] == D:
                self.is_defecting = True
                return D
            return C
    
    
    

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
        

        self.cooperation_count = 0
            
        self.is_defecting = True

    @classmethod
    def cooperate(cls, opponent: Player) -> Action:
        return C

    @classmethod
    def defect(cls, opponent: Player) -> Action:
        return D