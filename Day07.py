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

    def OuterBagCanContain(self, targetColors):
        Colors = []
        OuterColorsFound = [outer for outer, inner in self.rules.items() if len(set(targetColors).intersection(inner.keys())) > 0]
        Colors += OuterColorsFound
        if len(OuterColorsFound) > 0:
            Colors += self.OuterBagCanContain(OuterColorsFound)
        return list(set(Colors))

    def BagsRequired(self, color):
        InnerBags = 0
        InnerBags += sum([a + a*self.BagsRequired(c) for c, a in self.rules[color].items()])
        return InnerBags

    def SolvePartOne(self):
        return len(self.OuterBagCanContain(["shiny gold"]))


    def SolvePartTwo(self):
        return self.BagsRequired("shiny gold")

Display.DisplayAnswers(Day07(Resource(7)))