from AoC.Resource import Resource
from AoC import Display
from AoC import Puzzle
import re

class Day07(Puzzle.Puzzle):
    rules = {}

    def PrepareData(self):
        self.data = self.Resource.SplitLines().Get()
        for r in self.data:
            outer, inner = r.split(" contain ", maxsplit=1)
            self.rules[outer.replace(" bags", "")] = {y:int(x) for x,y in re.compile("(\d+) ([A-z\s]+) bags?").findall(inner)}

    def PossibleColors(self, targetColors):
        Colors = [outer for outer, inner in self.rules.items() if len(set(targetColors).intersection(inner.keys())) > 0]
        Colors += self.PossibleColors(Colors) if len(Colors) > 0 else []
        return list(set(Colors))

    def BagsInside(self, color):
        return sum([a + a*self.BagsInside(c) for c, a in self.rules[color].items()])

    def SolvePartOne(self):
        return len(self.PossibleColors(["shiny gold"]))

    def SolvePartTwo(self):
        return self.BagsInside("shiny gold")

Display.DisplayAnswers(Day07(Resource(7)))