class FoxProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)
        self.chicken_total = start_state[0]
        self.fox_total = start_state[1]
        self.boat_total = start_state[2]

        # you might want to add other things to the problem,
        #  like the total number of chickens (which you can figure out
        #  based on start_state

    # get successor states for the given state
    def get_successors(self, state):
        successor_list = []
        # moves satisfying at least 2 animals on boat - boat not included bc either switches to 0 or 1 depending on side
        valid_moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]

        for i in valid_moves:
            # defining how many chickens,foxes are moving to other side
            chicken_move, fox_move = i

            # checking what side boat is on
            if state[2] == 1:
                # set the new state decreasing num of chickens and foxes, boat on left
                new_state = (state[0] - chicken_move, state[1] - fox_move, 0)
            else:
                # set the new state increasing num of chickens and foxes, boat on right
                new_state = (state[0] + chicken_move, state[1] + fox_move, 1)

            # check if new state is valid and add to successors
            if self.valid_state(new_state):
                successor_list.append(new_state)

        #  you write is part. I also had a helper function
        #  that tested if states were safe before adding to successor list
        return successor_list
    # I also had a goal test method. You should write one.

    # check if state is goal state
    def goal_test(self, state):
        if state == self.goal_state:
            return True
        else:
            return False

    # check if state is valid state
    def valid_state(self, state):
        # set variables for animals on left and right sides
        right_chickens, right_foxes, boat = state
        left_chickens = self.start_state[0] - right_chickens
        left_foxes = self.start_state[1] - right_foxes

        # check chickens in danger on either side
        if left_foxes > left_chickens > 0 or right_foxes > right_chickens > 0:
            return False

        # check chickens in danger on left side
        # if right_foxes > right_chickens > 0:
            # return False

        # check that boundaries of total animals are not surpassed on either side
        if not (self.chicken_total >= left_chickens >= 0 and self.chicken_total >= right_chickens >= 0 and
                self.fox_total >= left_foxes >= 0 and self.fox_total >= right_foxes >= 0):
            return False

        return True

    def __str__(self):
        string = "Chickens and foxes problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_cp = FoxProblem((5, 5, 1))
    print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)
