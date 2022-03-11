# Melissa Valencia
# CS 76 AI, Fall 2021
import numpy as np


# filtering algorithm following description in AIMA textbook
def filtering(ev, model):
    probabilities = []
    # state set to uniform probability
    state = model.prior()

    # loop through evidence: colors
    for i in ev:
        # find color's matrix in color dictionary
        updated_model = model.color_dict[i]
        # update state using matrix multiplication: updated_model * (model.transition * state)
        state = np.dot(updated_model, np.dot(model.transition, state))
        # normalize updated state to ensure matrix sums to 1
        normalized_state = normalize(state)
        # add new probability distribution to list of probabilities
        probabilities.append(normalized_state)

    return probabilities


def normalize(matrix):
    m_sum = matrix.sum()
    normalized = matrix / m_sum
    return normalized
