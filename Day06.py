from AoC.Resource import Resource
from AoC import Display
from AoC import Puzzle
import numpy as np
import operator
import functools

class Day06(Puzzle.Puzzle):

    def PrepareData(self):
        self.data = [x.strip().split(" ") for x in self.Resource.Get().replace("\n\n", ";").replace("\n", " ").split(";")]

    def SolvePartOne(self):
        return np.sum([len(set("".join(x))) for x in self.data])

    def SolvePartTwo(self):
        return np.sum([len(functools.reduce(operator.and_, [set(x) for x in p])) for p in [g for g in self.data]])

Display.DisplayAnswers(Day06(Resource(6)))