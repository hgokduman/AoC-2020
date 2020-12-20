from AoC import Utils, Puzzle, Resource
import math

class Day20(Puzzle.Puzzle):
    tiles = {}
    arranged = None
    stack = None
    def transposed(self, tile):
        return list(''.join(row) for row in zip(*tile))

    def reversed_tile(self, tile):
        return [''.join(reversed(row)) for row in tile]

    def group(self, tile):
        return self.rotations(tile) + self.rotations(self.transposed(tile))

    def rotations(self, tile):
        ans = [tile]
        for _ in range(3):
            ans.append(self.reversed_tile(self.transposed(ans[-1])))
        return ans


    def PrepareData(self):
 

        self.data = self.Resource.Get().split("\n\n")
        for tile in self.data:
            lines = tile.split("\n")
            tile_id = int(lines[0].strip("Tile ").strip(":"))
            rows = lines[1:]
            self.tiles[tile_id] = self.group(rows)

    def ArrangeTiles(self):
        if not self.stack:
            return True
        (r, c) = self.stack.pop()
        for tile_id in list(self.tiles):
            tile_group = self.tiles[tile_id]
            del self.tiles[tile_id]
            for tile in tile_group:
                if r > 0:
                    if self.arranged[r - 1][c][1][-1] != tile[0]:
                        continue
                if c > 0:
                    if list(row[-1] for row in self.arranged[r][c - 1][1]) != list(row[0] for row in tile):
                        continue
                self.arranged[r][c] = (tile_id, tile)
                if self.ArrangeTiles():
                    return self.arranged[0][0][0] * self.arranged[-1][0][0] * self.arranged[0][-1][0] * self.arranged[-1][-1][0]
            self.tiles[tile_id] = tile_group
        self.stack.append((r, c))

    def SolvePartOne(self):
        self.n = int(math.sqrt(len(self.tiles)))
        self.arranged = [[0] * self.n for _ in range(self.n)]
        self.stack = list(reversed(list((r, c) for c in range(self.n) for r in range(self.n))))
        return self.ArrangeTiles()

    def SolvePartTwo(self):
        remove_border = lambda tile: [row[1:-1] for row in tile[1:-1]]
        get = lambda r,c: board[r // tile_n][c // tile_n][r % tile_n][c % tile_n]
        board = [[remove_border(tile[1]) for tile in row] for row in self.arranged]
        tile_n = len(board[0][0])
        board = [''.join(get(r, c) for c in range(self.n * tile_n)) for r in range(self.n * tile_n)]

        for pattern in self.group(
            ['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']):
            matches = 0
            for dr in range(len(board) - len(pattern) + 1):
                for dc in range(len(board[0]) - len(pattern[0]) + 1):
                    matches += all(pattern[r][c] == ' ' or board[r + dr][c + dc] == '#'
                                for r in range(len(pattern))
                                for c in range(len(pattern[0])))
            if matches:
                return ''.join(board).count('#') - ''.join(pattern).count('#') * matches
                break

if __name__ == '__main__':
    Utils.ShowAnswers(Day20(Resource.Resource(20)))