from Sudoku import Sudoku
# Melissa Valencia
# CS 76 AI, Fall 2021
# this code was provided from class
import sys

if __name__ == "__main__":
    test_sudoku = Sudoku()

    test_sudoku.load(sys.argv[1])
    print(test_sudoku)

    puzzle_name = sys.argv[1][:-4]
    cnf_filename = puzzle_name + ".cnf"

    test_sudoku.generate_cnf(cnf_filename)
    print("Output file: " + cnf_filename)

