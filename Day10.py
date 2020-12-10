from AoC.Resource import Resource
from AoC import Display, Puzzle
import numpy as np
from itertools import groupby
from functools import reduce 
import operator

class Day10(Puzzle.Puzzle):
    gaps = []

    def PrepareData(self):
        self.data = sorted([int(x) for x in self.Resource.SplitLines().Get()])

    def SolvePartOne(self):
        self.gaps = list(np.diff([0] + self.data + [max(self.data)+3]))
        return self.gaps.count(1)*self.gaps.count(3)

    def SolvePartTwo(self):
        seq = [len(list(values)) for gap,values in groupby(self.gaps) if gap==1]
        return reduce(operator.mul, [7 if x == 4 else 4 if x == 3 else x for x in seq if x != 1])
                
if __name__ == '__main__':
    Display.DisplayAnswers(Day10(Resource(10)))