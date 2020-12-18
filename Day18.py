from AoC import Utils, Puzzle, Resource
import re

class Day18(Puzzle.Puzzle):
    def PrepareData(self):
        self.numbers = [str(x) for x in range(0,10)]
        self.operators = ["+", "*"]
        self.data = [x.replace(" ", "").strip() for x in self.Resource.SplitLines().Get()]


    def replace_parentheses(self, line, part=1):
        if not(re.search(r'[\(\)]', line)):
            return self.calculate(line, part)

        expression = re.search(r'\(([0-9 +*]+)\)', line).group(1)
        result = self.calculate(expression, part)
        line = line.replace(f"({expression})", str(result))
        return self.replace_parentheses(line, part)
    
    
    def calculate(self, line, part=1):
        if not(re.search(r'[\+\*]', line)):
            return int(line)
        if part == 1:
            # find first expression, replace with calculation
            expression = re.search(r'\d+[\+\*]\d+', line).group(0)
        else:
            # find first expression, replace with calculation
            if re.search(r'\d+\+\d+', line):
                expression = re.search(r'\d+\+\d+', line).group(0)
            elif re.search(r'\d+\*\d+', line):
                expression = re.search(r'\d+\*\d+', line).group(0)

        result = eval(expression)
        line = line.replace(expression, str(result), 1)
        return int(self.calculate(line, part))


    def SolvePartOne(self):
        return sum([self.replace_parentheses(line, 1) for line in self.data])

    def SolvePartTwo(self):
        return sum([self.replace_parentheses(line, 2) for line in self.data])

if __name__ == '__main__':
    Utils.ShowAnswers(Day18(Resource.Resource(18)))