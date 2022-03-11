# You write this:
from SensorlessProblem import SensorlessProblem
from Maze import Maze

from uninformed_search import bfs_search
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

test_maze3 = Maze("maze3.maz")
test_sp = SensorlessProblem(test_maze3)
#
# print(test_mp.get_successors(test_mp.start_state))

# this should explore a lot of nodes; it's just uniform-cost search
result = astar_search(test_sp, null_heuristic)
print(result)
test_sp.animate_path(result.path)

result = astar_search(test_sp, test_sp.grid_heuristic)
print(result)
test_sp.animate_path(result.path)

test_maze4 = Maze("maze4.maz")
test_sp = SensorlessProblem(test_maze4)
result = astar_search(test_sp, test_sp.grid_heuristic)
print(result)
test_sp.animate_path(result.path)

test_maze5 = Maze("maze5.maz")
test_sp = SensorlessProblem(test_maze5)
result = astar_search(test_sp, test_sp.grid_heuristic)
print(result)
test_sp.animate_path(result.path)

test_maze6 = Maze("maze6.maz")
test_sp = SensorlessProblem(test_maze6)
result = astar_search(test_sp, test_sp.grid_heuristic)
print(result)
test_sp.animate_path(result.path)

test_maze7 = Maze("maze7.maz")
test_sp = SensorlessProblem(test_maze7)
result = astar_search(test_sp, test_sp.grid_heuristic)
print(result)
test_sp.animate_path(result.path)

test_maze8 = Maze("maze8.maz")
test_sp = SensorlessProblem(test_maze8)
result = astar_search(test_sp, test_sp.grid_heuristic)
print(result)
test_sp.animate_path(result.path)