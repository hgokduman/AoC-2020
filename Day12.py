from AoC.Resource import Resource
from AoC import Display, Puzzle

class Day12(Puzzle.Puzzle):
    heading = None
    ship = None
    waypoint = None
    
    def PrepareData(self):
        self.data = [(x[0], int(x[1:])) for x in self.Resource.SplitLines().Get()]

    def GetManhattanDistance(self):
        return abs(self.ship[0])+abs(self.ship[1])

    def Move(self, action, value, pos, multiplier=None):
        posX, posY = pos
        if action in ["N", "S"]:
            posY += value if action == "S" else -value
        elif action in ["E", "W"]:
            posX += value if action == "E" else -value
        elif action == "F":
            if multiplier is None:
                raise Exception ("No multiplier!")
            posX += value * multiplier[0]
            posY += value * multiplier[1]          

        return (posX, posY)
 
    def Rotate(self, action, value, pos):
        posX, posY = pos

        for _ in range(int(value/90)):
            newX = -posY if action == "R" else posY
            newY = posX if action == "R" else -posX
            posX, posY = (newX, newY)

        return (posX, posY)
        
    def SolvePartOne(self):       
        self.Reset()
        for action, value in self.data:
            if action in ["R", "L"]:
                self.heading = self.Rotate(action, value, self.heading)
            else:
                self.ship = self.Move(action, value, self.ship, self.heading)
        return self.GetManhattanDistance()

    def SolvePartTwo(self):
        self.Reset()
        for action, value in self.data:
            if action in ["F"]:
                self.ship = self.Move(action, value, self.ship, self.waypoint)
            elif action in ["E", "W", "N", "S"]:
                self.waypoint = self.Move(action, value, self.waypoint)
            elif action in ["R", "L"]:
                self.waypoint = self.Rotate(action, value, self.waypoint)
        return self.GetManhattanDistance()

    def Reset(self):
        self.heading = (1,0)
        self.ship = (0, 0)
        self.waypoint = (10, -1)

                
if __name__ == '__main__':
    Display.DisplayAnswers(Day12(Resource(12)))