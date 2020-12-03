class Puzzle:
    Resource = None

    def __init__(self, inp):
        self.Resource = inp
        self.PrepareData()

    def PrepareData(self):
        pass

    def SolvePartOne(self):
        pass

    def SolvePartTwo(self):
        pass
    
    def Reset(self):
        pass

    def Solve(self):
        return [self.SolvePartOne(), self.SolvePartTwo()]