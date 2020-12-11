from AoC.Resource import Resource
from AoC import Display, Puzzle
import copy
import itertools

FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]

class Day11(Puzzle.Puzzle):
    grid = None
    points = []
    gridWidth = 0
    gridHeight = 0

    def PrepareData(self):
        self.data = [x for x in self.Resource.SplitLines().Get()]
        self.Reset()
        self.gridHeight, self.gridWidth = len(self.grid), len(self.grid[0])
        self.points = list(itertools.chain.from_iterable([[(x,y) for y in range(self.gridHeight)] for x in range(self.gridWidth)]))

    def OccupiedAdjacentSeats(self, grid, x, y):
        checkPositions = [(x+moveX, y+moveY) for moveX, moveY in DIRECTIONS if 0 <= x+moveX < self.gridWidth and 0 <= y+moveY < self.gridHeight ]
        return sum([grid[posY][posX] == OCCUPIED for posX, posY in checkPositions])

    def OccupiedVisibleSeats(self, grid, x, y):
        checkPositions = []
        def FindFirstSeat(directionX, directionY):
            posX, posY = x, y
            while True:
                posX, posY = posX+directionX, posY+directionY
                if 0 <= posX < self.gridWidth and 0 <= posY < self.gridHeight:
                    if grid[posY][posX] != FLOOR:
                        return (posX, posY)
                else:
                    return None

        for moveX, moveY in DIRECTIONS:
            seat = FindFirstSeat(moveX, moveY)
            if seat is not None:
                checkPositions.append((seat[0], seat[1]))

        return sum([grid[posY][posX] == OCCUPIED for posX, posY in checkPositions])

    def Run(self, Part, Tolerance):
        self.Reset()
        Changed = None
        while Changed != 0:
            grid = copy.deepcopy(self.grid)
            Changed = 0
            for x,y in self.points:
                seat = grid[y][x]
                if not seat == FLOOR:
                    OccupiedSeats = self.OccupiedAdjacentSeats(grid, x, y) if Part == 1 else self.OccupiedVisibleSeats(grid, x, y)
                    if seat == EMPTY and OccupiedSeats == 0:
                        self.grid[y][x] = OCCUPIED
                        Changed += 1
                    elif seat == OCCUPIED and OccupiedSeats >= Tolerance:
                        self.grid[y][x] = EMPTY
                        Changed += 1
        
        return sum([sum([x == OCCUPIED for x in y]) for y in grid])

    def SolvePartOne(self):
        return self.Run(1, 4)

    def SolvePartTwo1(self):
        return self.Run(2, 5)

    def Reset(self):
        self.grid = [[s for s in x] for x in self.data]
                
if __name__ == '__main__':
    Display.DisplayAnswers(Day11(Resource(11)))