import AoC
import numpy as np
from itertools import permutations

entries = list(map(int, AoC.GetListFromInput(1)))

def Day01(length, target=2020):
    for x in permutations(entries, length):
        if sum(x) == target:
            return(np.prod(x))
        
AoC.ShowAnswers(Day01, [2, 3])