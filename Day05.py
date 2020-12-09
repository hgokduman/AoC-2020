from AoC.Resource import Resource
from AoC import Display
from AoC import Puzzle
import itertools 

class Day05(Puzzle.Puzzle):
    Seats = []
    
    def PrepareData(self):
        self.data = self.Resource.SplitLines().Get()
   
    def GetNumber(self, input):
        replacements = { "F": 0, "L": 0, "B": 1, "R": 1}
        for x,y in replacements.items():
            input = input.replace(x, str(y))
        return int(input, 2)

    def GetSeatId(self, seat):
        return (seat[0] * 8 + seat[1])

    def SolvePartOne(self):
        for p in self.data:
            seat = self.GetNumber(p[:7]), self.GetNumber(p[-3:])
            self.Seats.append((p, seat, self.GetSeatId(seat)))
        return (max([x for _, _, x in self.Seats]))

    def SolvePartTwo(self):
        AllSeats = list(map(self.GetSeatId, list(itertools.product(range(0, 128), range(0, 8)))))
        OccupiedSeats = [x for x in AllSeats if x in [a for _, _, a in self.Seats]]
        FreeSeats = [x for x in AllSeats if x not in OccupiedSeats]
        return list(filter(lambda x: x-1 in OccupiedSeats and x+1 in OccupiedSeats, FreeSeats))[0]

if __name__ == '__main__':
    Display.DisplayAnswers(Day05(Resource(5)))