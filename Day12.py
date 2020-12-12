from AoC.Resource import Resource
from AoC import Display, Puzzle
import copy
import itertools

class Day12(Puzzle.Puzzle):
    headings = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    heading = None
    ship = None
    waypoint = None
    
    def PrepareData(self):
        self.data = [(x[0], int(x[1:])) for x in self.Resource.SplitLines().Get()]

    def SolvePartOne(self):
        def Move(action, value):
            posX, posY = self.ship
            if action == "N":
                posY += -value
            elif action == "S":
                posY += value
            elif action == "E":
                posX += value
            elif action == "W":
                posX -= value
            elif action == "F":
                posX += value * self.heading[0]
                posY += value * self.heading[1]

            return (posX, posY)
        
        def Rotate(action, value):
            index = self.headings.index(self.heading)
            nextIndexOffset = int(value/90)
            if action == "L":
                index -= nextIndexOffset
            elif action == "R":
                index += nextIndexOffset
            return self.headings[index%len(self.headings)]

        self.Reset()
        for action, value in self.data:
            if action in ["R", "L"]:
                self.heading = Rotate(action, value)
            else:
                self.ship = Move(action, value)
        return sum(list(self.ship))

    def SolvePartTwo(self):
        self.Reset()
        def MoveShip(value):
            ShipX, ShipY = self.ship
            WayX, WayY = self.waypoint
            ShipX += WayX*value
            ShipY += WayY*value
            return (ShipX,ShipY)

        def Move(action, value):
            posX, posY = self.waypoint
            if action == "N":
                posY += -value
            elif action == "S":
                posY += value
            elif action == "E":
                posX += value
            elif action == "W":
                posX -= value

            return (posX, posY)

        def Rotate(action, value):
            newX, newY = (0,0)
            posX, posY = self.waypoint

            degrees  = value
            if degrees == 90:
                newX = -posY if action == "R" else posY
                newY = posX if action == "R" else -posX
            elif degrees == 180:
                newX = -posX
                newY = -posY
            elif degrees == 270:
                newX = posY if action == "R" else -posY
                newY = -posX if action == "R" else posX

            return (newX, newY)  

        for action, value in self.data:
            if action in ["F"]:
                self.ship = MoveShip(value)
            elif action in ["E", "W", "N", "S"]:
                self.waypoint = Move(action, value)
            elif action in ["R", "L"]:
                print(action, value)
                self.waypoint = Rotate(action, value)
        return sum(list(map(abs, list(self.ship))))


    def Reset(self):
        self.heading = (1,0)
        self.ship = (0, 0)
        self.waypoint = (10, -1)

                
if __name__ == '__main__':
    Display.DisplayAnswers(Day12(Resource(12)))