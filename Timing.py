from importlib import import_module
from AoC.Resource import Resource
import os
import sys

import datetime


def TimeIt(puzzleClass):
    timing = {}
    for method in ["SolvePartOne", "SolvePartTwo", "Solve"]:
        exec_start = datetime.datetime.now()
        obj = puzzleClass(Resource(int(module_name[-2:])))
        callMethod = getattr(obj, method)
        callMethod()
        exec_stop = datetime.datetime.now()
        exec_duration = (exec_stop - exec_start).microseconds/1000
        timing[method] = exec_duration
    
    return timing


for module_name in [x.name.replace(".py", "") for x in os.scandir(".") if x.name.startswith("Day") and x.name.endswith(".py")]:
    print(f"Importing module {module_name}")
    timing = TimeIt(getattr(import_module(module_name), module_name))
    for method, execution_time in timing.items():
        print(f"{method}: {execution_time}ms")