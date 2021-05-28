from itertools import product

"""
Find the probability of n number of dices (sum_) adding up to the amount (dice_amount)
"""


def rolldice_sum_prob(sum_, dice_amount):
    dices = [[i for i in range(1, 7)] for _ in range(dice_amount)]
    combinations = list(product(*dices))

    return len([combo for combo in combinations if sum(combo) == sum_]) / 6**dice_amount

assert rolldice_sum_prob(11, 2) == 0.05555555555555555
assert rolldice_sum_prob(8, 2) == 0.1388888888888889
assert rolldice_sum_prob(8, 3) == 0.09722222222222222
