import AoC
import numpy as np
from itertools import permutations

entries = list(map(int, AoC.GetListFromInput(1)))

def Day01(length):
    combinations = list(permutations(entries, length)) 
    for x in combinations:
        if sum(x) == 2020:
            return(np.prod(x))
        
print(Day01(2))
print(Day01(3))