from axelrod.action import Action, actions_to_str
from axelrod.player import Player
from axelrod.strategy_transformers import (
    FinalTransformer,
    TrackHistoryTransformer,
)

C, D = Action.C, Action.D


import os
os.environ["OPENAI_API_KEY"] = "sk-proj-Z3sDETRaTLPjL9ZyJqgMT3BlbkFJnvfv2WaBSnsUgKw4SLqh"


from openai import OpenAI
client = OpenAI()

class Parrot(Player):
    """
    A Statistical Parrot
    """

    # These are various properties for the strategy
    name = "Cardassian General"
    classifier = {
        "memory_depth": 10,  # Four-Vector = (1.,0.,1.,0.)
        "stochastic": False,
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
        # First move
        if not self.history:
            return C

        print(self.history)
        print(opponent.history)
                

        completion = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "system", "content": "You are a player of axelrod's tournament. You play against another player."},
            {"role": "user", "content": "A D stands for Defect. A C stands for Cooperate. The following is the history of actions of your opponent: " + str(opponent.history) + ". The following is the history of actions of yourself: " + str(self.history) + ". What do you do? Respond with either D or C."}
          ]
        )

        if completion.choices[0].message.content == "C":
            return C
        else:
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