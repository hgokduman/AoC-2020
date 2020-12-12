from AoC import Utils, Puzzle, Resource
import numpy as np
from itertools import permutations

class Day01(Puzzle.Puzzle):
    def PrepareData(self):
        self.data = self.Resource.SplitLines().Numeric().Get()

    def GetSumOfMultiplication(self, length, target=2020):
        self.Reset()
        for x in permutations(self.data, length):
            if sum(x) == target:
                return(np.prod(x))

    def SolvePartOne(self):
        return self.GetSumOfMultiplication(2)

    def SolvePartTwo(self):
        return self.GetSumOfMultiplication(3)

if __name__ == '__main__':
    Utils.ShowAnswers(Day01(Resource.Resource(1)))