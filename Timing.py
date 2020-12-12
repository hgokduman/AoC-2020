from importlib import import_module
from AoC.Resource import Resource
import os

for module_name in sorted([x.name.replace(".py", "") for x in os.scandir(".") if x.name.startswith("Day") and x.name.endswith(".py")]):
    print(f"Importing module {module_name}")
    resource = Resource(int(module_name[-2:]))
    puzzle = getattr(import_module(module_name), module_name)(resource)
    for i, val in enumerate(puzzle.Solve()):
        if val is not None:
            _, exec_time = val
            print(f"Part {i+1}: {exec_time:0.3f}ms")