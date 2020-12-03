from AoC.Resource import Resource
from AoC import Display
from AoC import Puzzle
import numpy as np

class Day03(Puzzle.Puzzle):
    Trees = 0
    posX, posY = [0, 0]

    def PrepareData(self):
        self.data = self.Resource.SplitLines().Get()
        self.length = len(self.data)
        self.width = len(self.data[0])

    def CountNumberOfTrees(self, slope):
        self.Reset()
        right, down = slope

        while True:
            self.Trees += 1 if self.data[self.posY][self.posX] == "#" else 0
            self.posX = (self.posX+right) % len(self.data[self.posY])
            self.posY += down
            if self.posY >= len(self.data):
                break

        return (self.Trees)

    def SolvePartOne(self):
        return self.CountNumberOfTrees((3,1))

    def SolvePartTwo(self):
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        return (np.prod(list(map(self.CountNumberOfTrees, slopes))))

    def Reset(self):
        self.posX, self.posY = [0, 0]
        self.Trees = 0

Display.DisplayAnswers(Day03(Resource(3)))
##### Another approach from T.Net #####
#from functools import reduce
#from itertools import count
#from operator import mul
#def count_trees(slope):
#   slope_right, slope_down = slope
#   return sum([self.data[i][j % self.width] == '#' for i, j in zip(range(slope_down, self.length, slope_down), count(slope_right, slope_right))])
#part two: return (reduce(mul, [self.CountNumberOfTrees(slope) for slope in slopes]))