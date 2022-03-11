# Author: Melissa Valencia, along with code provided from class
# CS 76 AI, Fall 2021
import random
import sys

from SATInstance import SATInstance


# class for sat solver, gsat and walksat
class SAT(SATInstance):
    def __init__(self, cnf_file, threshold=0.8):
        # pass in SATInstance
        super().__init__(cnf_file)
        self.threshold = threshold

    # general sat func, either gsat_dict or wsat_list passed in
    def sat(self, limit, v_list):
        count = 0
        satisfied_clauses = self.num_satisfied()

        # go through all satisfied clauses
        while satisfied_clauses != len(self.clauses):
            if count < limit:
                random.seed()

                # choose variable from given, either gsat_dict or wsat_list
                variable, overall_satisfied = self.choose_variable(v_list())
                # flip the variables
                self.variables[variable] = not self.variables[variable]

                satisfied_clauses += overall_satisfied
                count += 1

        # check if all clauses are satisfied, meaning there is a set assignment
        if self.num_satisfied() == len(self.clauses):
            print("count", count)
            return True
        return False

    # calculate all satisfied clauses
    def num_satisfied(self):
        total_satisfied = 0
        for clause in self.clauses:
            if self.valid_clause(clause):
                total_satisfied += 1
        return total_satisfied

    # check satisfiability of every clause
    def valid_clause(self, clause):
        for var in clause:
            if self.variables[var] == clause[var]:
                return True
        return False

    # chooses variable from either gsat_dict or wsat_list for general sat func
    def choose_variable(self, var_list):
        if random.random() > self.threshold:
            variable_list = list(var_list)
            var = random.choice(variable_list)
            overall_satisfied = self.get_overall_satisfied(var)

        else:
            # most satisfied clauses variables
            best_vars = []
            overall_satisfied = float('-inf')

            for var in var_list:
                curr_satisfied = self.get_overall_satisfied(var)

                if curr_satisfied > overall_satisfied:
                    # set best to new variable
                    best_vars = [var]
                    overall_satisfied = curr_satisfied
                elif curr_satisfied == overall_satisfied:
                    # equal to best, so add to list
                    best_vars.append(var)
            # choose from best
            var = random.choice(best_vars)

        return var, overall_satisfied

    # scoring the variables
    def get_overall_satisfied(self, var):
        satisfied_before = 0

        for clause in self.domains[var]:
            if self.valid_clause(clause):
                # how many clauses before flipping variable
                satisfied_before += 1

        # flip the variables
        self.variables[var] = not self.variables[var]

        satisfied_after = 0

        for clause in self.domains[var]:
            if self.valid_clause(clause):
                # how many clauses after flipping variable
                satisfied_after += 1

        # flip the variables
        self.variables[var] = not self.variables[var]

        overall_satisfied = satisfied_after - satisfied_before

        # calculate net satisfied
        return overall_satisfied

    # gsat variable selection, selects from all variables
    def gsat_dict(self):
        gsat_dict = dict()
        for i, variable in enumerate(self.variables):
            gsat_dict[i] = variable
        return gsat_dict

    # walksat variable selection, selects from unsatisfied clause
    def wsat_list(self):
        # creates list based off of unsatisfied clauses and chooses randomly
        choice = random.choice([clause for clause in self.clauses
                                if not self.valid_clause(clause)])
        return choice

    # gsat: calls general sat with gsat dict
    def gsat(self):
        gsat = self.sat(100000, self.gsat_dict)
        return gsat

    # walksat: calls general sat with walksat list
    def wsat(self):
        wsat = self.sat(100000, self.wsat_list)
        return wsat


if __name__ == "__main__":
    sat = SAT(sys.argv[1])
    # sat.gsat()
    sat.wsat()
