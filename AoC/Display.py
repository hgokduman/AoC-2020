import datetime

def DisplayAnswers(obj):
    exec_start = datetime.datetime.now()
    for i, val in enumerate(obj.Solve()):
        exec_stop = datetime.datetime.now()
        print(f"Part {i+1}: {val}")
    
    exec_duration = (exec_stop - exec_start).total_seconds()
    print(f"Executed in {exec_duration} seconds.")