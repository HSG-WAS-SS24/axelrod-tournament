import axelrod as axl
from wasstrategies import danai_strategy as pl0
from wasstrategies import marco_strategy as pl1
from wasstrategies import jonas_strategy as pl2
from wasstrategies import karim_strategy as pl3
from wasstrategies import david_strategy as pl4
from wasstrategies import stephan_strategy as pl5
from wasstrategies import dan_strategy as pl6
from wasstrategies import simon_strategy as pl7
from wasstrategies import simon_parrot_strategy as pl8
from wasstrategies import alessandro_strategy as pl9

"""Run an Axelrod Tournament (https://axelrod.readthedocs.io/en/stable/tutorials/new_to_game_theory_and_or_python/tournament.html)"""
# Create the strategy players
strategies = [
    axl.Cooperator(),
    axl.Defector(),
    axl.TitForTat(),
    axl.Grudger(),
    pl0.Danai(),
    pl1.Marco(),
    pl2.Jonas(),
    pl3.Karim(),
    pl3.Karim2(),
    pl4.David(),
    pl5.Stephan(),
    pl6.Dan(),
    pl7.Cardassian(),
    pl8.Parrot(),
    pl9.Alessandro()
]

# Print the startegy players
print(f"Available strategies: {strategies}")

# Play on the prisoner's dilemma: a = -1, b = -5, c = 0, d = -3
prisoners_dilemma = axl.game.Game(r=-1, s=-5, t=0, p=-3)

# Create the tournament between strategy players with 10 turns
tournament = axl.Tournament(strategies, game=prisoners_dilemma, turns=10, repetitions=1)

# Play the tournament
results = tournament.play(filename="was-tournament/was_tournament_analysis.csv")

# Print the players from the best to the worst
print(f"\nRanked results: {results.ranked_names}\n")


"""Visualize interactions (https://axelrod.readthedocs.io/en/stable/tutorials/new_to_game_theory_and_or_python/visualising_results.html)"""
plot = axl.Plot(results)

# View the scores averaged per opponent and turns
p1 = plot.boxplot()
p1.show()
p1.savefig("was-tournament/was_results.png")

# View the distributions of wins for each strategy
p2 = plot.winplot()
p2.show()
p2.savefig("was-tournament/was_win_distributions.png")

# View the payoff matrix
p2 = plot.payoff()
p2.show()
p2.savefig("was-tournament/was_payoff_matrix.png")


"""Morality metrics (https://axelrod.readthedocs.io/en/latest/how-to/calculate_morality_metrics.html#morality-metrics)"""

print("--- Morality Metrics ---")
for i in range(0, len(strategies)):
    print(strategies[i], ":")
    print(f"Cooperating rating: {round(results.cooperating_rating[i], 2)}")
    print(f"Good partner rating: {round(results.good_partner_rating[i], 2)}")
    print(f"Eigen Jesus rating: {round(results.eigenjesus_rating[i], 2)}")
    print(f"Eigen Moses rating: {round(results.eigenmoses_rating[i], 2)}\n")
