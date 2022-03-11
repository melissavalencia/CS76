# Melissa Valencia
# CS 76 AI, Fall 2021
# this code was provided from class
from Sudoku import Sudoku
import sys

def display_sudoku_solution(filename):

    test_sudoku = Sudoku()
    test_sudoku.read_solution(filename)
    print(test_sudoku)

if __name__ == "__main__":
    print(sys.argv[1])
    display_sudoku_solution(sys.argv[1])