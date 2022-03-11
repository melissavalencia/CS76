# Melissa Valencia
# CS 76 AI, Fall 2021
from Maze import Maze
import numpy as np
import random


class Robot:
    def __init__(self, maze):
        self.maze = maze
        self.transition = self.get_transition()
        self.color_dict = {'r': None, 'g': None, 'b': None, 'y': None}
        self.set_dict_colors()

    # setting probabilities for each color in color dict to track each color's matrix
    def set_dict_colors(self):
        # loop through the color dictionary
        for color in self.color_dict.keys():
            # initialize identity matrix
            color_matrix = np.identity(16)
            index = 0
            # loop through maze
            for j in range(self.maze.width):
                for k in range(self.maze.height):
                    # if matching color set probability to 0.88
                    if self.maze.what_color(j, k) == color:
                        color_matrix[index][index] = 0.88
                    # not matching color set probability to 0.04
                    else:
                        color_matrix[index][index] = 0.04
                    index += 1
            # update the color's matrix in color dictionary
            self.color_dict[color] = color_matrix

    # getting the successors: the possible positions based on given state coordinates
    def get_successors(self, state):
        # moves can be N, S, E, W
        valid_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        successors = []

        # loop over valid moves
        for move in valid_moves:
            position = tuple(map(lambda i, j: i + j, state, move))
            # check position's validity
            if not self.maze.is_floor(*position):
                successors.append(state)
            else:
                successors.append(position)
        return successors

    # generates evidence and path of length based on num steps given
    def generate_path(self, steps, start=(0, 0)):
        ev = []
        path = [start]
        state = start

        # loop through given num of steps
        for step in range(steps):
            if step != 0:
                # set the state to a random successor
                state = random.choice(self.get_successors(state))
                # add the state to the path
                path.append(state)
            # get the start state's color
            color = self.maze.what_color(*state)
            # check the probability based on 0.88 of detecting the correct color and append it to evidence
            if random.random() < 0.88:
                ev.append(color)
            # if incorrect color, choose random color and append it to evidence
            else:
                colors = ['r', 'g', 'b', 'y']
                colors.remove(color)
                random_color = random.choice(colors)
                ev.append(random_color)
        return ev, path

    # getting transition matrix for filtering
    def get_transition(self):
        matrix = np.zeros((16, 16))
        # loop through maze
        for i in range(self.maze.width):
            for j in range(self.maze.height):
                row = i * self.maze.width + j
                for pos in self.get_successors((i, j)):
                    position = pos[0] * self.maze.width + pos[1]
                    matrix[row][position] += 0.25
        # returns matrix with probabilities of moving from each position
        return matrix

    # returns starting matrix where robot has not made any moves, thus uniform probability
    def prior(self):
        return np.full((16, 1), 0.0625)

if __name__ == '__main__':
    maze = Maze("maze1.maz")
    problem = Robot(maze)
    # print(problem.color_dict['y'])
    print(problem.generate_path(4))
