import os

def _GetFileName(day):
    return(f"input/{day:02d}.txt")

def GetStringFromInput(day):
    with open(_GetFileName(day), "r") as f:
        return f.read()

def GetListFromInput(day):
    return GetStringFromInput(day).splitlines()

def ShowAnswers(func, listOfArgs):
    answers = map(func, listOfArgs)
    for i, val in enumerate(answers):
        print(f"Part {i+1}: {val}")