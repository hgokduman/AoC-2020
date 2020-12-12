from AoC import Utils, Puzzle, Resource
from itertools import combinations

class Day09(Puzzle.Puzzle):
    def PrepareData(self):
        self.data = [int(x) for x in self.Resource.SplitLines().Get()]

    def FindInvalidNumber(self, preambleSize):
        for i in range(preambleSize, len(self.data)):
            sets = [sum(x) for x in combinations(self.data[i-25:i], 2)]
            if self.data[i] not in sets:
                return (i, self.data[i])

    def FindContiguousSet(self, InvalidNumber, Index):
        dataset = self.data[:Index]

        for i in range(Index):
            for s in range(Index-1):
                currentSet = dataset[i:s]
                if sum(currentSet) == InvalidNumber:
                    return currentSet

        return None

    def SolvePartOne(self):
        _, Number = self.FindInvalidNumber(25)
        return Number

    def SolvePartTwo(self):
        Index, Number = self.FindInvalidNumber(25)
        ContiguousSet = self.FindContiguousSet(Number, Index)
        return min(ContiguousSet)+max(ContiguousSet)
                
if __name__ == '__main__':
    Utils.ShowAnswers(Day09(Resource.Resource(9)))