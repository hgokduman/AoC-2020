import datetime

def DisplayAnswers(func, listOfArgs):
    answers = map(func, listOfArgs)
    for i, val in enumerate(listOfArgs):
        exec_start = datetime.datetime.now()
        answer = func(val)
        exec_stop = datetime.datetime.now()
        exec_duration = (exec_stop - exec_start).total_seconds()
        print(f"Part {i+1}: {answer} - executed in {exec_duration} seconds.")