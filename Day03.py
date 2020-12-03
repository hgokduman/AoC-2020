from AoC.Resource import Resource
from AoC import Display
from AoC import Puzzle
import numpy as np

class Day03(Puzzle.Puzzle):
    Trees = 0
    posX, posY = [0, 0]

    def CountNumberOfTrees(self, right, down):
        self.Reset()

        while True:
            self.Trees += 1 if self.GetValue(self.posY, self.posX) == "#" else 0
            self.posX = (self.posX+right) % len(self.data[self.posY])
            self.posY += down
            if self.posY >= len(data):
                break

        return (self.Trees)

    def GetValue(self, y, x):
        return (self.data[y][x])

    def SolvePartOne(self):
        return self.CountNumberOfTrees(3, 1)

    def SolvePartTwo(self):
        return(np.prod(list(map(self.CountNumberOfTrees, [1, 3, 5, 7, 1], [1, 1, 1, 1, 2]))))

    def Reset(self):
        self.posX, self.posY = [0, 0]
        self.Trees = 0

data = Resource(3).SplitLines().Get()
Display.DisplayAnswers(Day03(data))