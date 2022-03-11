# Melissa Valencia
# CS 76 AI, Fall 2021
# this code was provided from class
import random
import sys

from SAT import SAT
from display import display_sudoku_solution

if __name__ == "__main__":
    # for testing, always initialize the pseudorandom number generator to output the same sequence
    #  of values:
    random.seed(1)

    puzzle_name = str(sys.argv[1][:-4])
    sol_filename = puzzle_name + ".sol"

    sat = SAT(sys.argv[1])
    w_result = sat.wsat()
    if w_result:
        sat.write_solution(sol_filename)
        display_sudoku_solution(sol_filename)


