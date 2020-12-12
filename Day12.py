from AoC.Resource import Resource
from AoC import Display, Puzzle
import copy
import itertools


class Day12(Puzzle.Puzzle):
    heading = (1,0)
    headings = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    posX = 0
    posY = 0
    
    def PrepareData(self):
        self.data = [(x[0], int(x[1:])) for x in self.Resource.SplitLines().Get()]

    def Move(self, action, value):
        if action == "N":
            self.posY += -value
        elif action == "S":
            self.posY += value
        elif action == "E":
            self.posX += value
        elif action == "W":
            self.posX -= value
        elif action == "F":
            self.posX += value * self.heading[0]
            self.posY += value * self.heading[1]
    
    def Rotate(self, action, value):
        index = self.headings.index(self.heading)
        nextIndexOffset = int(value/90)
        if action == "L":
            index -= nextIndexOffset
        elif action == "R":
            index += nextIndexOffset
        self.heading = self.headings[index%len(self.headings)]

    def SolvePartOne(self):
        for action, value in self.data:
            if action in ["R", "L"]:
                self.Rotate(action, value)
            else:
                self.Move(action, value)
        return abs(self.posX)+abs(self.posY)
                
if __name__ == '__main__':
    Display.DisplayAnswers(Day12(Resource(12)))