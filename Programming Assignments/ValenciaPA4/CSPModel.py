# Author: Melissa Valencia
# CS 76 AI, Fall 2021

from abc import abstractmethod


class CSPModel:

    def __init__(self, variables, domains, constraints, domain_dict):
        self.variables = variables
        # set of just domain values
        self.domains = domains
        # keeping track of all variables neighbors for constraints
        self.constraints = constraints
        # dictionary of all variables domain values
        self.domain_dict = domain_dict
        self.backtrack_calls = 0

    # checking assigned value consistency by checking all neighbors assignments so far, defined in each problem
    @abstractmethod
    def check_consistency(self, variable, value, assignment):
        pass

    # selects an unassigned variable for backtracking
    def select_unassigned_variable(self, assignment, heuristic):
        if heuristic == "None":
            for v in self.variables:
                if v not in assignment:
                    return v
        elif heuristic == "MRV":
            return self.minimum_remaining_value(assignment)
        elif heuristic == "DH":
            return self.degree(assignment)

    # set domain values for each variable
    def order_domain_values(self, variable, heuristic):
        if heuristic == "None":
            return self.domains
        if heuristic == "LCV":
            return self.least_constraining_value(variable)

    def inference(self):
        return True

    def backtracking_search(self, var_heuristic, dom_heuristic):
        assignment = dict()
        return self.backtrack(assignment, var_heuristic, dom_heuristic)

    def backtrack(self, assignment, var_heuristic, dom_heuristic):
        self.backtrack_calls += 1
        if len(assignment) == len(self.variables):
            return assignment
        variable = self.select_unassigned_variable(assignment, var_heuristic)
        ordered_domain = self.order_domain_values(variable, dom_heuristic)
        for value in ordered_domain:
            if self.check_consistency(variable, value, assignment):
                assignment[variable] = value
                if self.inference():
                    inferences = self.ac3()
                    if inferences:
                        result = self.backtrack(assignment, var_heuristic, dom_heuristic)
                        if result is not None:
                            return result
                else:
                    result = self.backtrack(assignment, var_heuristic, dom_heuristic)
                    if result is not None:
                        return result

                del assignment[variable]
        return None

    def ac3(self):
        edges = set()

        for v in self.variables:
            for neighbor in self.constraints[v]:
                edges.add((v, neighbor))

        while edges:
            (var_i, var_j) = edges.pop()
            if self.revise(var_i, var_j):
                if len(self.domain_dict[var_i]) == 0 or len(self.domain_dict[var_j]) == 0:
                    return False
                for neighbor in (self.constraints[var_i]):
                    if neighbor != var_j:
                        edges.add((neighbor, var_i))
        return True

    def revise(self, var_i, var_j):
        revised = False
        for x in self.domain_dict[var_i]:
            constraint_satisfied = False
            for y in self.domain_dict[var_j]:
                if x != y:
                    constraint_satisfied = True
            if not constraint_satisfied:
                self.domain_dict[var_i].remove(x)
                revised = True
        return revised

    # calculating number of conflicts based on possible domain values left
    def num_conflicts(self, variable, value):
        conflicts = 0
        for neighbor in self.constraints[variable]:
            if len(self.domain_dict[neighbor]) > 1 and value in self.domain_dict[variable]:
                conflicts += 1
        return conflicts

    # lcv heuristic, choosing least constraining domain value
    def least_constraining_value(self, variable):
        if len(self.domain_dict[variable]) == 1:
            return self.domain_dict[variable]

        sort_by = lambda value: self.num_conflicts(variable, value)
        return sorted(self.domain_dict[variable], key=sort_by)

    # mrv heuristic, choose one with minimum value choices left
    def minimum_remaining_value(self, assignment):
        mrv = None
        for v in self.domain_dict:
            if v not in assignment:
                if not mrv or len(self.domain_dict[v]) < len(self.domain_dict[mrv]):
                    mrv = v
        return mrv

    # degree heuristic, choosing one with most constraints
    def degree(self, assignment):
        mc = None
        len_mc = -1
        for v in self.variables:
            if v not in assignment:
                if not mc or len_mc < len(self.constraints[v]):
                    mc = v
                    len_mc = len(self.constraints[v])
        return mc
