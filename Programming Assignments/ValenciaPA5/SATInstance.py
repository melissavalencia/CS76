# Author: Melissa Valencia
# CS 76 AI, Fall 2021
# class for representing a problem, reads input cnf file and encodes clauses
import random


class SATInstance:
    def __init__(self, cnf_file):
        self.variables = []
        self.clauses = []
        self.encode = dict()
        self.domains = dict()
        self.parse_add_clauses(cnf_file)

    # encodes the clauses, adds them to clause list as dictionaries and sets domains
    def parse_add_clauses(self, cnf_file):
        cnf = open(cnf_file)

        # set clause list by going through all clauses in cnf, then each literal within every line in file
        # calls encode_literal func and checks negation to then add to each clause dict within clause list
        self.clauses = [{self.encode_literal(literal): literal[0] != "-"
                         for literal in clause.split()}
                        for clause in cnf]

        # set domains for each variable, useful for sat implementation, ensuring there aren't unnecessary clauses
        self.domains = {var: [clause for clause in self.clauses
                              if var in clause]
                        for var in range(len(self.variables))}

        cnf.close()

    def encode_literal(self, literal):
        # removing negation
        if literal[0] == "-":
            literal = literal[1:]

        # check if it has already been encoded
        if literal not in self.encode:
            # set in encode dict
            self.encode[literal] = len(self.variables)
            # random assignment
            self.variables.append(bool(random.getrandbits(1)))

        return self.encode[literal]

    # writing out solution to file
    def write_solution(self, sol_filename):
        decode = {value: key for key, value in self.encode.items()}

        solution = open(sol_filename, "w")

        for i, variable in enumerate(self.variables):
            if variable:
                solution.write("{}\n".format(decode[i]))

        solution.close()
