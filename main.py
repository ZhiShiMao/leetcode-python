import sys
from solution_wrapper import solution_wrapper

filename = sys.argv[1]
if filename:
    with open(filename, "r") as file:
        exec(file.read())
        solution_wrapper(eval("Solution"))()