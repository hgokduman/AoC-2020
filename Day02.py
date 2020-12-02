from AoC.Resource import Resource
from AoC import Display

data = Resource(2).SplitLines().RegEx("([0-9]+)\-([0-9]+) ([A-z])\: ([A-z]+)").Get()

def Day02(part=1):
    validPasswords = 0
    for PolicyNrOne, PolicyNrTwo, PolicyChar, Password in data:
        if part == 1:
            if int(PolicyNrOne) <= Password.count(PolicyChar) <= int(PolicyNrTwo):
                validPasswords += 1
        elif part == 2:
            if (Password[int(PolicyNrOne)-1] == PolicyChar) ^ (Password[int(PolicyNrTwo)-1] == PolicyChar):
                validPasswords += 1
    return(validPasswords)

Display.DisplayAnswers(Day02, [1, 2])