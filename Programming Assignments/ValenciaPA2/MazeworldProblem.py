from Maze import Maze
from time import sleep
from math import *


class MazeworldProblem:

    ## you write the constructor, and whatever methods your astar function needs

    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goal_locations = goal_locations
        self.start_state = tuple([0]+maze.robotloc)
        self.num_robots = len(goal_locations) // 2

    # get successor states of the current state
    def get_successors(self, state):

        # updating maze
        self.maze.robotloc = list(state[1:])

        # moves can be N, S, E, W
        valid_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # get info from state
        current_robot = state[0]
        next_robot = (current_robot + 1) % self.num_robots
        current_position = state[2 * current_robot + 1:2 * current_robot + 3]

        successor_list = [tuple([next_robot])+state[1:]]

        for i in valid_moves:
            # robot's updated position adopted from https://www.kite.com/python/answers/how-to-add-tuples-in-python
            updated_position = tuple(map(sum, zip(current_position, i)))

            # checking position validity
            if self.maze.is_floor(updated_position[0], updated_position[1]) and not self.maze.has_robot(
                    updated_position[0], updated_position[1]):
                new_state = tuple([next_robot]) + state[1:2 * current_robot + 1] + updated_position + state[
                    2 * current_robot + 3:]
                successor_list.append(new_state)

        return successor_list

    # check if current state contains goals
    def goal_test(self, state):
        if self.goal_locations == state[1:]:
            return True
        else:
            return False

    def calculate_cost(self, current, new):
        # check if robots moved
        state = current.state
        if list(state[1:]) == list(new[1:]):
            # 0 bc they didn't move
            cost = current.transition_cost
        else:
            # 1 bc they moved
            cost = current.transition_cost + 1
        return cost

    # manhattan heuristic function
    def manhattan_heuristic(self, state):
        heuristic = 0
        for i in range(self.num_robots):
            heuristic += abs(self.goal_locations[2 * i] - state[2 * i + 1]) + abs(
                self.goal_locations[2 * i + 1] - state[2 * i + 2])
        return heuristic

    def __str__(self):
        string = "Mazeworld problem: "
        return string

        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))


## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    print(test_mp.get_successors((0, 1, 0, 1, 2, 2, 1)))
