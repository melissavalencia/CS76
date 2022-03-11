from collections import deque
from SearchSolution import SearchSolution
from FoxProblem import FoxProblem


# you might find a SearchNode class useful to wrap state objects,
#  keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        # you write this part
        self.state = state
        self.parent = parent


# you might write other helper functions, too. For example,
#  I like to separate out backchaining, and the dfs path checking functions

def bfs_search(search_problem):
    # if search_problem.goal_test():
    #     return search_problem
    queue = deque([SearchNode(search_problem.start_state)])
    # queue.append(search_problem)
    # initialize explored set with start state
    explored = {search_problem.start_state}
    solution = SearchSolution(search_problem, "bfs")

    while len(queue) > 0:
        # pop vs popleft
        current_node = queue.popleft()
        # current_state = FoxProblem(current_node.state)

        # check if this is the goal state
        if search_problem.goal_test(current_node.state):
            # backchain from current node
            solution.nodes_visited = len(explored)
            solution.path = backchaining(current_node)
            break

        for successors in search_problem.get_successors(current_node.state):
            if successors not in explored:
                explored.add(successors)
                child_node = SearchNode(successors, current_node)
                queue.append(child_node)
    solution.nodes_visited = len(explored)

    return solution

# helper for bfs backchaining to get path from goal state to start state
def backchaining(current_node):
    path = [current_node.state]

    while current_node.parent is not None:
        current_node = current_node.parent
        # add state to the beginning of the path list
        path.insert(0, current_node.state)

    return path


# Don't forget that your dfs function should be recursive and do path checking,
#  rather than memoizing (no visited set!) to be memory efficient

# We pass the solution along to each new recursive call to dfs_search
#  so that statistics like number of nodes visited or recursion depth
#  might be recorded
def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    # if no node object given, create a new search from starting state
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")

    # add node to current solution
    solution.path.append(node.state)
    solution.nodes_visited += 1

    # check if current node's state is goal state
    if search_problem.goal_test(node.state):
        return solution

    # check if depth limit has been reached
    if len(solution.path) == depth_limit:
        return solution

    # you write this part
    for successors in search_problem.get_successors(node.state):

        # check if successor is in solution path
        if successors not in solution.path:
            successor_node = SearchNode(successors, node)
            possible_solution = dfs_search(search_problem, depth_limit, successor_node, solution)

            # check if last state in possible solution's path is a goal state
            if search_problem.goal_test(possible_solution.path[-1]):
                return possible_solution

    # if node is not part of solution path
    solution.path.remove(node.state)
    return solution


def ids_search(search_problem, depth_limit=100):
    node = SearchNode(search_problem.start_state)
    solution = SearchSolution(search_problem, "IDS")

    # you write this part
    for i in range(depth_limit):
        # store first possible solution returned from dfs
        possible_solution = dfs_search(search_problem, i, node, solution)
        # update final solution nodes visited
        solution.nodes_visited += possible_solution.nodes_visited

        # check if a path exists using length from what dfs returns
        if len(possible_solution.path) > 0:
            # update final solution path
            solution.path = possible_solution.path
            break
    return solution
