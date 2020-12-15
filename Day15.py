from AoC import Utils, Puzzle, Resource

class Day15(Puzzle.Puzzle):

    def PrepareData(self):
        self.data = [int(x) for x in self.Resource.Get().strip().split(",")]

    def Run(self, seq, nth):
        n, seen, val, seq_length = 0, {}, 0, len(seq)
        while n < nth-1:
            if n < seq_length:
                val = seq[n]
            last = {val: n}
            val = n - seen.get(val, n)
            seen.update(last)
            n += 1
        return val

    def SolvePartOne(self):
         return self.Run(self.data, 2020)

    def SolvePartTwoa(self):
        return self.Run(self.data, 30000000)

if __name__ == '__main__':
    Utils.ShowAnswers(Day15(Resource.Resource(15)))