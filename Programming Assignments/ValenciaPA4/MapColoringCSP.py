# Author: Melissa Valencia
# CS 76 AI, Fall 2021

from CSPModel import CSPModel


class MapColoringCSP(CSPModel):
    def __init__(self, m_variables, m_domains, m_constraints, dom_dict):
        self.m_variables = m_variables
        self.m_domains = m_domains
        self.m_constraints = m_constraints
        self.dom_dict = dom_dict

        for v in self.m_variables:
            dom_dict[v] = self.m_domains

        super().__init__(self.m_variables, self.m_domains, self.m_constraints, self.dom_dict)

    # checking that neighbor constraint is satisfied
    def check_consistency(self, variable, value, assignment):
        if assignment is None:
            return False
        for v in self.constraints[variable]:
            if v in assignment:
                if value == assignment[v]:
                    return False
        return True


if __name__ == "__main__":
    variables = ["WA", "NT", "SA", "QU", "NSW",
                 "VI", "TA"]
    domains = ["red", "green", "blue"]
    constraints = {"WA": ["NT", "SA"], "NT": ["WA", "SA", "QU"], "SA": ["WA", "NT", "QU", "NSW", "VI"],
                   "QU": ["NT", "SA", "NSW"], "NSW": ["QU", "SA", "VI"], "VI": ["SA", "NSW"], "TA": []}

    domain_dict = dict()

    map_csp = MapColoringCSP(variables, domains, constraints, domain_dict)
    variable_heuristic = "MRV"
    domain_heuristic = "None"

    solution = CSPModel.backtracking_search(map_csp, variable_heuristic, domain_heuristic)

    print(solution)
    print("backtrack calls", map_csp.backtrack_calls)

    map_csp2 = MapColoringCSP(variables, domains, constraints, domain_dict)
    variable_heuristic = "DH"
    domain_heuristic = "None"

    solution = CSPModel.backtracking_search(map_csp2, variable_heuristic, domain_heuristic)

    print(solution)
    print("backtrack calls", map_csp2.backtrack_calls)

    variables = ["WA", "NT", "SA", "QU", "NSW",
                 "VI", "TA"]
    domains = ["red", "green", "blue"]
    constraints = {"WA": ["NT", "SA"], "NT": ["WA", "SA", "QU"], "SA": ["WA", "NT", "QU", "NSW", "VI"],
                   "QU": ["NT", "SA", "NSW"], "NSW": ["QU", "SA", "VI"], "VI": ["SA", "NSW"], "TA": []}

    domain_dict = dict()

    map_csp3 = MapColoringCSP(variables, domains, constraints, domain_dict)
    variable_heuristic = "MRV"
    domain_heuristic = "LCV"

    solution = CSPModel.backtracking_search(map_csp3, variable_heuristic, domain_heuristic)

    print(solution)
    print("backtrack calls", map_csp3.backtrack_calls)

    variables = ["WA", "NT", "SA", "QU", "NSW",
                 "VI", "TA"]
    domains = ["red", "green", "blue"]
    constraints = {"WA": ["NT", "SA"], "NT": ["WA", "SA", "QU"], "SA": ["WA", "NT", "QU", "NSW", "VI"],
                   "QU": ["NT", "SA", "NSW"], "NSW": ["QU", "SA", "VI"], "VI": ["SA", "NSW"], "TA": []}

    domain_dict = dict()

    map_csp3 = MapColoringCSP(variables, domains, constraints, domain_dict)
    variable_heuristic = "DH"
    domain_heuristic = "LCV"

    solution = CSPModel.backtracking_search(map_csp3, variable_heuristic, domain_heuristic)

    print(solution)
    print("backtrack calls", map_csp3.backtrack_calls)
