def DisplayAnswers(func, listOfArgs):
    answers = map(func, listOfArgs)
    for i, val in enumerate(answers):
        print(f"Part {i+1}: {val}")