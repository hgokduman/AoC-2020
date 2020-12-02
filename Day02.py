from AoC.Resource import Resource
from AoC import Display

data = Resource(2).SplitLines().RegEx("([0-9]+)-([0-9]+) ([A-z]): ([A-z]+)").Get()

def Day02(part=1):
    validPasswords = 0
    for DigitOne, DigitTwo, Char, Password in data:
        validPasswords += 1 if part == 1 and int(DigitOne) <= Password.count(Char) <= int(DigitTwo) else 0
        validPasswords += 1 if part == 2 and (Password[int(DigitOne)-1] == Char) ^ (Password[int(DigitTwo)-1] == Char) else 0
    return(validPasswords)

Display.DisplayAnswers(Day02, [1, 2])