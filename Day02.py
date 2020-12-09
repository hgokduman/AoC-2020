from AoC.Resource import Resource
from AoC import Display
from AoC import Puzzle

class Day02(Puzzle.Puzzle):
    validPasswords = 0

    def PrepareData(self):
        self.data = self.Resource.SplitLines().RegEx("([0-9]+)-([0-9]+) ([A-z]): ([A-z]+)").Get()

    def SolvePartOne(self):
        self.Reset()
        for DigitOne, DigitTwo, Char, Password in self.data:
            self.validPasswords += 1 if int(DigitOne) <= Password.count(Char) <= int(DigitTwo) else 0
        return(self.validPasswords)

    def SolvePartTwo(self):
        self.Reset()
        for DigitOne, DigitTwo, Char, Password in self.data:
            self.validPasswords += 1 if (Password[int(DigitOne)-1] == Char) ^ (Password[int(DigitTwo)-1] == Char) else 0
        return(self.validPasswords)
        
    def Reset(self):
        self.validPasswords = 0

if __name__ == '__main__':
    Display.DisplayAnswers(Day02(Resource(2)))