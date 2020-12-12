from AoC import Utils, Puzzle, Resource
import re

class Day07(Puzzle.Puzzle):
    rules = {}

    def PrepareData(self):
        self.data = self.Resource.SplitLines().Get()
        for r in self.data:
            outer, inner = r.split(" bags contain ", maxsplit=1)
            self.rules[outer] = {y:int(x) for x,y in re.compile("([0-9]+) ([a-z ]+) bags?").findall(inner)}

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

if __name__ == '__main__':
    Utils.ShowAnswers(Day07(Resource.Resource(7)))