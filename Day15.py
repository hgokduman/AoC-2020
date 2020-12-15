from AoC import Utils, Puzzle, Resource
from itertools import islice

class Day15(Puzzle.Puzzle):

    def PrepareData(self):
        self.data = [int(x) for x in self.Resource.Get().strip().split(",")]

    def Run(self, seq):
        n, seen, val, seq_length = 0, {}, 0, len(seq)
        while True:
            if n < seq_length:
                val = seq[n]
            yield val
            last = {val: n}
            val = n - seen.get(val, n)
            seen.update(last)
            n += 1

    def SolvePartOne(self):
         return list(islice(self.Run(self.data), 2020))[-1]

    def SolvePartTwo(self):
        return list(islice(self.Run(self.data), 30000000))[-1]

if __name__ == '__main__':
    Utils.ShowAnswers(Day15(Resource.Resource(15)))