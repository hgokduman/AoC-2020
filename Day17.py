from AoC import Utils, Puzzle, Resource
import operator
from functools import reduce
import itertools

ACTIVE = "#"
INACTIVE = "."
class Day17(Puzzle.Puzzle):
    def CreateSpace(self, dimensions):
        space = set()
        for x, line in enumerate(self.Resource.SplitLines().Get()):
            for y, cell in enumerate(line.strip()):
                if cell == '#':
                    space.add((x, y) + (0,) * (dimensions - 2))
        return space

    def generate_points(self, low, high):
        if len(low) == 0:
            return [()]

        return [
            (i,) + subpoint
            for i in range(low[0] - 1, high[0] + 2)
            for subpoint in self.generate_points(low[1:], high[1:])
        ]


    def neighbors(self, point):
        dims = len(point)
        return [
            other_point
            for other_point in self.generate_points(
                point,
                point
            )
            if other_point != point
        ]
        
    def update_bounds(self, low, high, point):
        low = list(low)
        high = list(high)
        point = list(point)

        for i in range(len(low)):
            if point[i] <= low[i]:
                low[i] = point[i]
            if high[i] <= point[i]:
                high[i] = point[i]

        return tuple(low), tuple(high)
        
    def cycle(self, space, low, high, dimensions):
        new_space = set()
        new_low = (0,) * dimensions
        new_high = (0,) * dimensions
        for point in self.generate_points(low, high):
            active_neighbors = sum(
                1
                for neighbor in self.neighbors(point)
                if neighbor in space
            )
            if point in space and active_neighbors == 2 \
                    or active_neighbors == 3:
                new_space.add(point)
                new_low, new_high = self.update_bounds(new_low, new_high, point)

        return new_space, new_low, new_high

    def Run(self, dimensions, cycles):
        space = self.CreateSpace(dimensions)
        
        low = (0,) * dimensions
        high = (7, 7) + (0,) * (dimensions - 2)

        for _ in range(cycles):
            space, low, high = self.cycle(space, low, high, dimensions)

        return len(space)

    def SolvePartOne(self):
        return self.Run(3, 6)

    def SolvePartTwo(self):
        return self.Run(4, 6)

if __name__ == '__main__':
    Utils.ShowAnswers(Day17(Resource.Resource(17)))