from collections import Counter
from combinations import ScoringCombo, scoring_combos
from itertools import combinations_with_replacement
from typing import Iterable
import math
import argparse

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
    for dice in combinations_with_replacement(range(1, 7), num_dice):
        yield Counter(dice)

def scores_and_probs(num_dice: int, banked_score: int = 0) -> dict[int, float]:
    """Return the expected score for the given number of dice"""
    results = {}
    for dice_totals in enumerate_possible_dice_totals(num_dice):
        score = max_score(dice_totals)
        prob = probability(dice_totals, num_dice)
        if score != 0:
            score += banked_score
        if score not in results:
            results[score] = prob
        else:
            results[score] += prob
    return results



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num_dice", type=int, help="Number of dice to roll")
    parser.add_argument("--banked_score", type=int, default=0, help="Banked score")
    args = parser.parse_args()
    results = scores_and_probs(args.num_dice, banked_score=args.banked_score)
    for score, prob in sorted(results.items()):
        print(f"Score: {score}, Probability: {100*prob:.3f}")

    # expected score
    expected_score = sum(score * prob for score, prob in results.items())
    print(f"Expected score: {expected_score:.6f}")