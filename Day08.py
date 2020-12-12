from AoC import Utils, Puzzle, Resource

class Day08(Puzzle.Puzzle):
    instructions = []

    def PrepareData(self):
        self.data = self.Resource.SplitLines().Get()
        self.instructions = [(a, int(b)) for a, b in [tuple(x.split()) for x in self.data]]


    def Run(self, Code):
        def acc(line, acc, param):
            return (line+1, acc+param)

        def jmp(line, acc, aparamrg):
            return (line+param, acc)

        def nop(line, acc, param):
            return (line+1, acc)

        Functions = {"acc": acc, "jmp": jmp, "nop": nop}

        Line = 0
        Accumulator = 0
        Executed = []

        while Line < len(Code):
            func, param = Code[Line]
            if Line in Executed:
                break
            Executed.append(Line)
            Line, Accumulator = Functions[func](Line, Accumulator, param)

        return (Line == len(Code), Line, Accumulator)

    
    def SolvePartOne(self):
        _, _, Accumulator = self.Run(self.instructions)
        return Accumulator

    def SolvePartTwo(self):
        for i in range(len(self.instructions)):
            newInstructions = self.instructions.copy()
            func, arg = newInstructions[i]
            if func in ["nop", "jmp"]:
                func = "nop" if func == "jmp" else "jmp"
                newInstructions[i] = (func, arg)
                Completed, _, Accumulator = self.Run(newInstructions)

                if Completed:
                    return Accumulator

        return None

if __name__ == '__main__':        
    Utils.ShowAnswers(Day08(Resource.Resource(8)))