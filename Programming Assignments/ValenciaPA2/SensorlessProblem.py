from Maze import Maze
from time import sleep


class SensorlessProblem:

    ## You write the good stuff here:
    def __init__(self, maze):
        self.maze = maze
        self.start_state = self.calculate_start_state(maze)

    def __str__(self):
        string = "Blind robot problem: "
        return string

    # returns all possible locations of robot
    def calculate_start_state(self, maze):
        possible_locations = []
        for x in range(maze.height):
            for y in range(maze.width):
                # checks that the location coordinate is valid
                if maze.is_floor(x, y):
                    possible_locations.append(x)
                    possible_locations.append(y)
        return tuple(possible_locations)

    def get_successors(self, state):
        self.maze.robotloc = state

        successor_list = []

        # moves can be N, S, E, W
        valid_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in valid_moves:
            successors = set()
            for j in range(len(state) // 2):
                current_position = (state[2 * j], state[2 * j + 1])
                updated_position = tuple(map(sum, zip(current_position, i)))

                # check validity of position
                if self.maze.is_floor(updated_position[0], updated_position[1]):
                    current_position = updated_position

                successors.add(current_position)

            # flatten tuple adapted from https://www.geeksforgeeks.org/python-flatten-tuple-of-list-to-tuple/
            successor_list.append(tuple(sum(successors,())))

        return successor_list

    def calculate_cost(self, current, new):
        cost = current.transition_cost + 1
        return cost

    # first test heuristic function
    def test_heuristic(self, state):
        heuristic = len(state)
        return heuristic

    # more optimal heuristic function
    def grid_heuristic(self, state):
        upper_x, upper_y, lower_x, lower_y = 0, 0, float('inf'), float('inf')

        for i in range(len(state)//2):
            if state[2*i] < lower_x:
                lower_x = state[2*i]
            if state[2*i+1] < lower_y:
                lower_y = state[2*i+1]
            if state[2*i] > upper_x:
                upper_x = state[2*i]
            if state[2*i+1] > upper_y:
                upper_y = state[2*i]
        # -1 to ensure admissibility
        width = upper_x - lower_x - 1
        height = upper_y - lower_y - 1
        heuristic = width + height
        return heuristic

    # check that a robot's location (x,y) has been found
    def goal_test(self, state):
        if len(state) == 2:
            return True
        else:
            return False

        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(1)

            print(str(self.maze))


## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
