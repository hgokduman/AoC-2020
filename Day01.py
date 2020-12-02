from AoC.Resource import Resource
from AoC import Display

import numpy as np
from itertools import permutations

data = Resource(1).SplitLines().Numeric().Get()

def Day01(length, target=2020):
    for x in permutations(data, length):
        if sum(x) == target:
            return(np.prod(x))

Display.DisplayAnswers(Day01, [2, 3])