from AoC.Resource import Resource
from AoC import Display
from AoC import Puzzle

import numpy as np
from itertools import permutations

class Day01(Puzzle.Puzzle):
    def GetSumOfMultiplication(self, length, target=2020):
        self.Reset()
        for x in permutations(self.data, length):
            if sum(x) == target:
                return(np.prod(x))

    def SolvePartOne(self):
        return self.GetSumOfMultiplication(2)

    def SolvePartTwo(self):
        return self.GetSumOfMultiplication(3)

data = Resource(1).SplitLines().Numeric().Get()
Display.DisplayAnswers(Day01(data))