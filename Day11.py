from AoC.Resource import Resource
from AoC import Display, Puzzle
import copy

FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"
DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]

class Day11(Puzzle.Puzzle):
    grid = None
    gridWidth = 0
    gridHeight = 0

    def PrepareData(self):
        self.data = [x for x in self.Resource.SplitLines().Get()]

    def AdjacentSeats(self, grid, x, y):
        checkPositions = [(x+moveX, y+moveY) for moveX, moveY in DIRECTIONS if 0 <= x+moveX < self.gridWidth and 0 <= y+moveY < self.gridHeight ]
        occupiedSeats = sum([grid[posY][posX] == OCCUPIED for posX, posY in checkPositions])
        return occupiedSeats

    def SolvePartOne(self):
        self.Reset()
        def ApplyRules():
            Changes = 0
            grid = copy.deepcopy(self.grid)
            for y in range(self.gridHeight):
                for x in range(self.gridWidth):
                    seat = grid[y][x]
                    if not seat == FLOOR:
                        adjacentSeats = self.AdjacentSeats(grid, x, y)
                    if seat == EMPTY and adjacentSeats == 0:
                        self.grid[y][x] = OCCUPIED
                        Changes += 1
                    elif seat == OCCUPIED and adjacentSeats >= 4:
                        self.grid[y][x] = EMPTY
                        Changes += 1
        
            OccupiedSeats = sum([sum([x == OCCUPIED for x in y]) for y in grid])
            return (Changes, OccupiedSeats)
        
        while True:
            Changes, Occupied = ApplyRules()
            if Changes == 0:
                return Occupied

    def VisibleSeats(self, grid, x, y):
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

        occupiedSeats = sum([grid[posY][posX] == OCCUPIED for posX, posY in checkPositions])
        return occupiedSeats

    def SolvePartTwo(self):
        self.Reset()
        def ApplyRules():
            Changes = 0
            grid = copy.deepcopy(self.grid)
            for y in range(self.gridHeight):
                for x in range(self.gridWidth):
                    seat = grid[y][x]
                    if not seat == FLOOR:
                        visibleSeats = self.VisibleSeats(grid, x, y)
                    if seat == EMPTY and visibleSeats == 0:
                        self.grid[y][x] = OCCUPIED
                        Changes += 1
                    elif seat == OCCUPIED and visibleSeats >= 5:
                        self.grid[y][x] = EMPTY
                        Changes += 1
        
            OccupiedSeats = sum([sum([x == OCCUPIED for x in y]) for y in grid])
            return (Changes, OccupiedSeats)
        
        while True:
            Changes, Occupied = ApplyRules()
            if Changes == 0:
                return Occupied

    def Reset(self):
        self.grid = [[s for s in x] for x in self.data]
        self.gridHeight, self.gridWidth = len(self.grid), len(self.grid[0])
                
if __name__ == '__main__':
    Display.DisplayAnswers(Day11(Resource(11)))