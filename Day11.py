from AoC import Utils, Puzzle, Resource
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
        self.seats = [(x,y) for x,y in self.points if self.grid[y][x] != FLOOR]

    def OccupiedAdjacentSeats(self, x, y):
        return sum([0<=x+moveX<self.gridWidth and 0<=y+moveY<self.gridHeight and self.grid[y+moveY][x+moveX] == OCCUPIED for moveX, moveY in DIRECTIONS])

    def OccupiedVisibleSeats(self,  x, y):
        checkPositions = []
        def FindFirstSeat(directionX, directionY):
            posX, posY = x, y
            while True:
                posX, posY = posX+directionX, posY+directionY
                return (posX, posY) if 0<=posX<self.gridWidth and 0<=posY<self.gridHeight and self.grid[posY][posX] in [EMPTY, OCCUPIED] else None

        for moveX, moveY in DIRECTIONS:
            seat = FindFirstSeat(moveX, moveY)
            if seat is not None:
                checkPositions.append((seat[0], seat[1]))

        return sum([self.grid[posY][posX] == OCCUPIED for posX, posY in checkPositions])

    def Run(self, Part, Tolerance, checkFunc):
        self.Reset()
        Changed = None
        while Changed != 0:
            swap = [(x,y, self.grid[y][x]) for x,y in self.seats if (self.grid[y][x] == EMPTY and checkFunc(x, y) == 0) or (self.grid[y][x] == OCCUPIED and checkFunc(x, y) >= Tolerance)]
            for x,y,seat in swap:
                self.grid[y][x] = OCCUPIED if seat == EMPTY else EMPTY 
            Changed = len(swap)
        
        return sum([sum([x == OCCUPIED for x in y]) for y in self.grid])

    def SolvePartOne(self):
        return self.Run(1, 4, self.OccupiedAdjacentSeats)

    def SolvePartTwo(self):
        return self.Run(2, 5, self.OccupiedVisibleSeats)

    def Reset(self):
        self.grid = [[s for s in x] for x in self.data]
                
if __name__ == '__main__':
    Utils.ShowAnswers(Day11(Resource.Resource(11)))