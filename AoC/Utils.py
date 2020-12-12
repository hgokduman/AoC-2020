import datetime
import time

def ShowAnswers(obj):
    solutions = obj.Solve()
    answer_max_length = max([len(str(x[0])) for x in solutions if x is not None])
    for i, val in enumerate(solutions):
        answer, exec_time = val
        answer = format(answer, f"{answer_max_length}d")
        print(f"Part {i+1}: {answer} in {exec_time:0.3f}ms")