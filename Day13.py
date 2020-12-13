from AoC import Utils, Puzzle, Resource

class Day13(Puzzle.Puzzle):
    earliest_ts = None
    buses = None
    
    def PrepareData(self):
        self.data = [x for x in self.Resource.SplitLines().Get()]
        self.earliest_ts = int(self.data[0])
        self.buses = [(t, int(b)) for t,b in enumerate(self.data[1].split(",")) if b != "x"]
        
    def SolvePartOne(self):       
        waitingTimes = [(b, (b-self.earliest_ts)%b) for _,b in self.buses]
        busId, waitingTime = sorted(waitingTimes, key=lambda x:x[1])[0]
        return busId*waitingTime

    def SolvePartTwo(self):       
        ts = 0
        increment = 1
        for t, b in self.buses:
            while ((ts+t)%b):
                ts += increment
            increment *= b
        return ts
              
if __name__ == '__main__':
    Utils.ShowAnswers(Day13(Resource.Resource(13)))