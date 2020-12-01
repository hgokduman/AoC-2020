import AoC
import numpy as np
from itertools import permutations

entries = list(map(int, AoC.GetListFromInput(1)))

def Day01(length, target=2020):
    combinations = list(permutations(entries, length)) 
    for x in combinations:
        if sum(x) == target:
            return(np.prod(x))
        
print(Day01(2))
print(Day01(3))