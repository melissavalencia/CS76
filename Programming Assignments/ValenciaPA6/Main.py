# Melissa Valencia
# CS 76 AI, Fall 2021
# testing file
from Maze import Maze
from Robot import Robot
from HiddenMarkovModel import filtering
import numpy as np
import matplotlib.pyplot as plt


# initialize maze object, can change maze file to be any of the ones in this folder
maze = Maze("maze1.maz")
# initialize robot object with maze
robot = Robot(maze)
# get evidence of observed colors and path of robot positions
ev, path = robot.generate_path(3, (1, 1))
# call filtering algorithm on evidence and problem to get array of probability distribution matrices
probabilities = filtering(ev, robot)
print("The maze:")
print(robot.maze)
print("The Robot's path:")
print(path)
print("The probabilities at each step:")

# loop through the probabilities list
for i in probabilities:
    matrix = np.flip(100 * np.array(i).reshape(4, 4), 1)
    # print each probability distribution matrix
    print(matrix)

    # heatmaps showing maze positions that robot will most likely be in based on evidence
    plt.imshow(matrix, cmap='binary', interpolation='nearest')
    plt.axis('off')
    plt.show()
