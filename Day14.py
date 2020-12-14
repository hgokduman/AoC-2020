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
                k = Utils.Replace(k, ["mem[", "]"], "")
                m.append((int(k),int(v)))
        self.program.append((p, m))
       
    def doBitwise(self, bitmask, val, keepX=False):
        binval = [char for char in "{0:036b}".format(val)]
        if keepX:
            newVal = [bitmask[i] if bitmask[i] != "0" else binval[i] for i,x in enumerate(binval)]
            return "".join(newVal)
        else:
            newVal = [bitmask[i] if bitmask[i] != "X" else binval[i] for i,x in enumerate(binval)]       
            return int("".join(newVal), 2)

    def SolvePartOne(self):       
        for bitmask, code in self.program:
            for address, val in code:
                self.memory[address] = self.doBitwise(bitmask, val)
        return sum(self.memory.values())

    def getPermutations(self, bitmask, address):
        addresses = []
        address = self.doBitwise(bitmask, address, True)
        floating = [i for i,x in enumerate(address) if x == "X"]
        permutations = list(product("01",repeat=len(floating)))
        for p in permutations:
            a = [char for char in address]
            for i,b in enumerate(p):
                a[floating[i]] = b
            addresses.append(int("".join(a),2))
        return addresses

    def SolvePartTwo(self):
        self.Reset()
        for bitmask, code in self.program:
            for address, val in code:
                addresses = self.getPermutations(bitmask, address)
                for a in addresses:
                    self.memory[a] = val
        return sum(self.memory.values())

    def Reset(self):
        self.memory = {}

if __name__ == '__main__':
    Utils.ShowAnswers(Day14(Resource.Resource(14)))