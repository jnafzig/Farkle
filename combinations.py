
from collections import Counter
from pydantic import BaseModel

class ScoringCombo(BaseModel):
    combo: Counter
    score: int

# Farkle scoring combinations
scoring_combos: list[ScoringCombo] = [
    # Single dice
    ScoringCombo(combo=Counter({1:1}), score=100),
    ScoringCombo(combo=Counter({5:1}), score=50),
    # Three of a kind
    ScoringCombo(combo=Counter({1:3}), score=1000),
    ScoringCombo(combo=Counter({2:3}), score=200),
    ScoringCombo(combo=Counter({3:3}), score=300),
    ScoringCombo(combo=Counter({4:3}), score=400),
    ScoringCombo(combo=Counter({5:3}), score=500),
    ScoringCombo(combo=Counter({6:3}), score=600),
    # Straight
    ScoringCombo(combo=Counter({1:1, 2:1, 3:1, 4:1, 5:1, 6:1}), score=1500),
]

# add in three pair combinations
for i in range(1, 7):
    for j in range(i+1, 7):
        for k in range(j+1, 7):
            scoring_combos.append(ScoringCombo(combo=Counter({i:2, j:2, k:2}), score=500))

# add in two triplet combinations
for i in range(1, 7):
    for j in range(i+1, 7):
        scoring_combos.append(ScoringCombo(combo=Counter({i:3, j:3}), score=2500))
