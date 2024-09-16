from collections import Counter
from combinations import ScoringCombo, scoring_combos
from itertools import combinations
from typing import Iterable
import math

def max_score(dice_totals: Counter) -> int:
    """Return the maximum score for the given dice"""
    combos = [combo for combo in scoring_combos if combo.combo <= dice_totals]
    if not combos:
        return 0
    return max(combo.score + max_score(dice_totals - combo.combo) for combo in combos)

def probability(dice_totals: Counter, num_rolls: int) -> float:
    """Return the probability of scoring with the given dice in the given number of rolls"""
    ways = 1
    rolls_left = num_rolls
    for total in dice_totals.values():
        ways *= math.comb(rolls_left, total)
        rolls_left -= total
        if rolls_left < 0:
            return 0.0
    if rolls_left > 1:
        return 0.0 
    return ways / 6 ** num_rolls


def enumerate_possible_dice_totals(num_dice: int) -> Iterable[Counter]:
    """Yield all possible dice totals for the given number of dice"""
    for dice in combinations(range(1, 7), num_dice):
        yield Counter(dice)

if __name__ == "__main__":
    dice_totals = list(enumerate_possible_dice_totals(3))
    for dice_total in dice_totals:
        assert sum(dice_total.values()) == 3
    unique_dice_totals = set(tuple(dice_total.most_common()) for dice_total in dice_totals)
    print(len(unique_dice_totals), len(dice_totals))