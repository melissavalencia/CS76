# Author: Melissa Valencia
# CS 76 AI, Fall 2021

from CSPModel import CSPModel
from CircuitBoard import CircuitRectangle
from CircuitBoard import CircuitBoard


class CircuitCSP(CSPModel):

    def __init__(self, c_variables, c_domains, c_constraints, dom_dict):
        self.c_variables = c_variables
        self.c_domains = c_domains
        self.c_constraints = c_constraints
        self.dom_dict = dom_dict

        # indicate index of variable for dict conversion
        self.variable_dict_rev = dict()

        # indicate index of domain value for consistency lookup
        self.index_dict_rev = dict()

        for index, var in enumerate(self.c_variables):
            self.variable_dict_rev[var] = index
            self.index_dict_rev[index] = var

        # board dimensions
        self.board_width = max([val[0] for val in self.c_domains]) + 1
        self.board_height = max([val[1] for val in self.c_domains]) + 1

        super().__init__(self.c_variables, self.c_domains, self.c_constraints, self.dom_dict)

    # checking for overlaps in boards
    def check_consistency(self, variable, value, assignment):

        count = 0
        if value[0] + variable.width > self.board_width or value[1] + variable.height > self.board_height:
            return False
        for neighbor in self.constraints[variable]:
            if neighbor in assignment:
                rectangle_pos = assignment[neighbor]
                if variable.intersects(value, neighbor, rectangle_pos, (self.board_width, self.board_height)) != 0:
                    intersections = variable.intersects(value, neighbor, rectangle_pos,
                                                        (self.board_width, self.board_height))
                    count = count + intersections
            if count > 0:
                return False
        return True


if __name__ == "__main__":
    # size of board
    width = 10
    height = 3
    # rectangle positions
    variables = [j := CircuitRectangle('j', 3, 2), k := CircuitRectangle('k', 5, 2), l := CircuitRectangle('l', 2, 3),
                 m := CircuitRectangle('m', 7, 1)]
    domain = [(x, y) for x in range(10) for y in range(3)]
    constraints = dict()
    domain_dict = dict()

    # setting domains
    for v in variables:
        domain_dict[v] = [(x, y) for x in range(10) for y in range(3)]

    # setting constraints
    for rectangle_i in variables:
        for rectangle_j in variables:
            if rectangle_i is not rectangle_j:
                if rectangle_i in constraints:
                    # adding to existing set
                    constraints[rectangle_i].add(rectangle_j)
                else:
                    # initializing set
                    constraints[rectangle_i] = {rectangle_j}

    circuit_csp = CircuitCSP(variables, domain, constraints, domain_dict)
    variable_heuristic = "DH"
    domain_heuristic = "None"

    solution = CSPModel.backtracking_search(circuit_csp, variable_heuristic, domain_heuristic)
    print(solution)

    board = CircuitBoard(width, height)

    # adding rectangles from solution to board
    for variable in solution:
        x = solution[variable][0]
        y = solution[variable][1]

        board.add_rectangle(variable, x, y)

    print(board)
