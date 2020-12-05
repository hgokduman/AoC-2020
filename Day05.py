from AoC.Resource import Resource
from AoC import Display
from AoC import Puzzle
import numpy as np
import itertools 

class Day05(Puzzle.Puzzle):
    Seats = []
    
    def PrepareData(self):
        self.data = self.Resource.SplitLines().Get()

    def GetNumber(self, input):
        Values = list(range(0, pow(2, len(input))))
        for x in input:
            HalfOfValues = int(len(Values)/2)
            Values = Values[:HalfOfValues] if x in ["F", "L"] else Values[-HalfOfValues:]
        return Values[0]

    def GetSeatId(self, seat):
        return (seat[0] * 8 + seat[1])

    def SolvePartOne(self):
        for p in self.data:
            seat = self.GetNumber(p[:7]), self.GetNumber(p[-3:])
            self.Seats.append((p, seat, self.GetSeatId(seat)))
        return (max([x for _, _, x in self.Seats]))


    def SolvePartTwo(self):
        AllSeats = list(itertools.product(range(0, 128), range(0, 8)))
        FreeSeats = [x for x in AllSeats if x not in [a for _, a, _ in self.Seats]]
        MySeat = [x for x in FreeSeats if 10 <= x[0] <= 100][0]
        return self.GetSeatId(MySeat)

Display.DisplayAnswers(Day05(Resource(5)))