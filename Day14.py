from AoC import Utils, Puzzle, Resource
from itertools import product

class Day14(Puzzle.Puzzle):
    program = []
    memory = {}
    def PrepareData(self):
        self.data = [x for x in self.Resource.SplitLines().Get()]
        p = None
        m = None
        for line in self.data:
            k,v = line.split(" = ")
            if k == "mask":
                if p is not None:
                    self.program.append((p, m))
                p = v
                m = []
            else:
                k = k.lstrip("mem[").rstrip("]")
                m.append((int(k),int(v)))
        self.program.append((p, m))

    def SumOfMemoryValues(self):
        return sum(self.memory.values())

    def int2bin(self, value, positions=None):
        return [char for char in ("{0:0b}".format(value) if positions is None else ("{0:0" + str(positions) + "b}").format(value))]
    
    def bin2int(self, value):
        val = "".join(value) if isinstance(value, list) else value
        return int(val, 2)

    def bitwise(self, value, bitmask, ignoreChars):
        binval = self.int2bin(value, 36)
        newVal = [bitmask[i] if bitmask[i] not in ignoreChars else binval[i] for i,x in enumerate(binval)]       
        return newVal

    def getPermutations(self, bitmask, address):
        addresses = []
        address = self.bitwise(bitmask, address, ["0"])
        floating = [i for i,x in enumerate(address) if x == "X"]
        permutations = list(product("01",repeat=len(floating)))
        for p in permutations:
            a = [char for char in address]
            for i,b in enumerate(p):
                a[floating[i]] = b
            addresses.append(int("".join(a),2))
        return addresses

    def SolvePartOne(self):       
        for bitmask, code in self.program:
            for address, value in code:
                self.memory[address] = self.bin2int(self.bitwise(value, bitmask, ["X"]))
        return self.SumOfMemoryValues()

    def SolvePartTwo(self):
        self.Reset()
        for bitmask, code in self.program:
            for address, value in code:
                addresses = self.getPermutations(address, bitmask)
                for a in addresses:
                    self.memory[a] = value
        return self.SumOfMemoryValues()

    def Reset(self):
        self.memory = {}

if __name__ == '__main__':
    Utils.ShowAnswers(Day14(Resource.Resource(14)))