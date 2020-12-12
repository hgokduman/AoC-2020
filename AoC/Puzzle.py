#import AoC.Utils
import time
class Puzzle:
    Resource = None

    def __init__(self, inp):
        self.Resource = inp
        self.PrepareData()

    def PrepareData(self):
        pass

    def timeit(method):
        def timed(*args, **kw):
            ts = time.time()
            result = method(*args, **kw)
            te = time.time()
            return (result, (te-ts)*1000)
        return timed

    @timeit
    def PartOne(self):
        if hasattr(self.__class__, "SolvePartOne"):
            return self.SolvePartOne()
        else:
            return None

    @timeit
    def PartTwo(self):
        if hasattr(self.__class__, "SolvePartTwo"):
            return self.SolvePartTwo()
        else:
            return None

    def Reset(self):
        pass

    def Solve(self):
        return [self.PartOne(), self.PartTwo()]