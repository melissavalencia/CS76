# Author: Melissa Valencia
# CS 76 AI, Fall 2021

# class for an entire board
class CircuitBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        # list that represents the board in 1d
        self.board_points = self.height * self.width * ['.']

        # list of all coordinate positions on board
        self.board_coord = [(x, y) for x in range(self.height) for y in range(self.width)]

    # add a rectangle to the board
    def add_rectangle(self, rectangle_i, x, y):

        # all of rectangles positions
        rectangle_pos = rectangle_i.get_rectangle_pos(x, y, (self.width, self.height))

        # assign rectangle name to the positions
        for position in rectangle_pos:
            self.board_points[self.index(*position)] = rectangle_i.var

    # get index from board_points
    def index(self, x, y):
        return (self.height - y - 1) * self.width + x

    # print board
    def __str__(self):
        s = '--board--\n'
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                s += self.board_points[self.index(x, y)]
            s += '\n'
        return s


# class for rectangles on board and their positions
class CircuitRectangle:
    def __init__(self, var, width, height):
        self.var = var
        self.width = width
        self.height = height
        self.x = None
        self.y = None

    # gives set containing positions that rectangle is on
    def get_rectangle_pos(self, start_x, start_y, board_size):
        return set([((start_x + x) % board_size[0], (start_y + y) % board_size[1]) for x in range(self.width) for y in range(self.height)])

    # checks intersection between boards
    def intersects(self, pos_1, board_2, pos_2, board_size):
        num_intersections = len(self.get_rectangle_pos(pos_1[0], pos_1[1], board_size).intersection(board_2.get_rectangle_pos(pos_2[0], pos_2[1], board_size)))
        return num_intersections

    def __repr__(self):
        return self.var


if __name__ == "__main__":

    board = CircuitBoard(10, 3)

    rectangle = CircuitRectangle('m', 7, 1)
    rectangle.x, rectangle.y = 1, 3
    board.add_rectangle(rectangle, 0, 0)
    rectangle_set = rectangle.get_rectangle_pos(1, 7, (board.width, board.height))

    print(rectangle_set)
    print(board)
