from SearchSolution import SearchSolution
from heapq import heappush, heappop
from priority_queue import PriorityQueue


class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        # you write this part
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.transition_cost = transition_cost

    def priority(self):
        # you write this part
        # establishing evaluation function
        priority = self.transition_cost + self.heuristic
        return priority

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result


def astar_search(search_problem, heuristic_fn):
    # I'll get you started:
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    # pqueue = []
    # heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    frontier = PriorityQueue()
    frontier.add_task(start_node)

    # you write the rest:
    #
    while frontier.pq:
        current_node = frontier.pop_task()
        solution.nodes_visited += 1

        # check if this node's state is the goal state
        if search_problem.goal_test(current_node.state):
            solution.path = backchain(current_node)
            solution.cost = current_node.transition_cost
            return solution

        # get this node's state's successors
        successors = search_problem.get_successors(current_node.state)
        for successor in successors:

            # pack the node up, updating its cost
            successor_node = AstarNode(successor, heuristic_fn(successor), current_node,
                                       search_problem.calculate_cost(current_node, successor))

            # check if this successors's state is the goal state
            if search_problem.goal_test(successor_node.state):
                solution.path = backchain(successor_node)
                solution.cost = successor_node.transition_cost
                return solution

            # add the successor to the frontier with the updated cost
            frontier.add_task(successor_node, successor_node.priority())

    return solution
