
import math
from collections import Counter
from farkle import probability, max_score, enumerate_possible_dice_totals

def test_probability():
    assert math.isclose(probability(Counter({1:1, 2:0, 3:0, 4:0, 5:0, 6:0}), 1), 1/6)
    assert math.isclose(probability(Counter({1:1, 2:1, 3:0, 4:0, 5:0, 6:0}), 2), 1/6**2 * 2)
    assert math.isclose(probability(Counter({1:1, 2:1, 3:1, 4:1, 5:1, 6:1}), 6), math.factorial(6) / 6**6)

def test_max_score():
    assert max_score(Counter({1:1, 2:0, 3:0, 4:0, 5:0, 6:0})) == 100
    assert max_score(Counter({1:1, 2:1, 3:0, 4:0, 5:1, 6:0})) == 150
    assert max_score(Counter({1:5, 2:1, 3:1, 4:1, 5:1, 6:1})) == 2600

def test_enumerate_possible_dice_totals(num_dice: int = 3):
    dice_totals = list(enumerate_possible_dice_totals(num_dice))
    for dice_total in dice_totals:
        assert sum(dice_total.values()) == num_dice

    unique_dice_totals = set(tuple(dice_total.most_common()) for dice_total in dice_totals)
    assert len(unique_dice_totals) == len(dice_totals)
