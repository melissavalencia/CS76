from MazeworldProblem import MazeworldProblem
from Maze import Maze

from uninformed_search import bfs_search
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

test_maze3 = Maze("maze3.maz")
test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

print(test_mp.get_successors(test_mp.start_state))

# this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_mp, null_heuristic)
print(result)

# this should do a bit better:
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

# Your additional tests here:
test_maze4 = Maze("maze4.maz")
test_mp = MazeworldProblem(test_maze4, (4, 4, 1, 2, 3, 5))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze5 = Maze("maze5.maz")
test_mp = MazeworldProblem(test_maze5, (2, 2, 7, 2, 5, 2))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze6 = Maze("maze6.maz")
test_mp = MazeworldProblem(test_maze6, (9, 5, 9, 4, 1, 0))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze7 = Maze("maze7.maz")
test_mp = MazeworldProblem(test_maze7, (8, 4, 13, 3, 5, 8))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)

test_maze8 = Maze("maze8.maz")
test_mp = MazeworldProblem(test_maze8, (0, 13, 18, 6, 5, 2))
result = astar_search(test_mp, test_mp.manhattan_heuristic)
print(result)
test_mp.animate_path(result.path)