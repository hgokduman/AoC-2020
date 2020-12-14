import datetime
import time

def ShowAnswers(obj):
    for i, val in enumerate(obj.Solve()):
        answer, exec_time = val
        if answer is not None:
            print(f"Part {i+1}: {answer} in {exec_time:0.3f}ms")

def Replace(FindIn, FindStr, ReplaceWith):
    if not isinstance(FindStr, list):
        FindStr = [FindStr]

    for i,r in enumerate(FindStr):
        replacement = ReplaceWith if not isinstance(ReplaceWith, list) else ReplaceWith[i]
        FindIn = FindIn.replace(r, replacement)

    return FindIn