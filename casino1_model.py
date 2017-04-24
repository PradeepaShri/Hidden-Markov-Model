import numpy as np

states = ('s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8')

possible_observations = ('1', '2', '3', '4', '5', '6',)

observation_sequence = (
        '1', '6', '3', '4', '1', '6', '3', '4', '3', '5', '1', '4', '6', '2', '5', '4', '2', '6', '3', '1',
        '5', '5', '2', '6', '4', '4', '2', '5', '1', '6', '2', '3', '4', '1', '3', '1', '6', '3', '1', '5',
        '5', '6', '4', '1', '6', '3', '6', '2', '6', '5', '1', '4', '2', '5', '6', '3', '4', '6', '2', '6',
        '3', '5', '6', '2', '6', '5', '3', '6', '1', '4', '5', '2', '6', '3', '5', '2', '6', '1', '5', '3',
        '4', '1', '6', '2', '6', '3', '5', '2')

prior_probability = np.matrix('1 0 0 0 0 0 0 0')

transition_probabilities = np.matrix([[0, 1, 0, 0, 0, 0, 0, 0],
                                        [0, 0, 1, 0, 0, 0, 0, 0],
                                        [0, 0, 0, 1, 0, 0, 0, 0],
                                        [0.75, 0, 0, 0, 0.25, 0, 0, 0],
                                        [0, 0, 0, 0, 0, 1, 0, 0],
                                        [0, 0, 0, 0, 0, 0, 1, 0],
                                        [0, 0, 0, 0, 0, 0, 0, 1],
                                        [0.25, 0, 0, 0, 0.75, 0, 0, 0]])


emission_probabilities = np.matrix([[0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                                              [0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                                              [0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                                              [0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                                              [0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                                              [0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                                              [0.167, 0.167, 0.167, 0.167, 0.167, 0.167],
                                              [0.167, 0.167, 0.167, 0.167, 0.167, 0.167]])
def get_states():
    return states

def get_possible_observations():
    return possible_observations

def get_observation_sequence():
    return observation_sequence

def get_transition_probabilties():
    return transition_probabilities

def get_emission_probabilities():
    return emission_probabilities

def get_prior_probabilty():
    return prior_probability

def get_state_dict(states):
    state_dict = {}
    for i, o in enumerate(states):
        state_dict[i] = o
    return state_dict

def get_observation_dict(observations):
    obs_dict = {}
    for i, o in enumerate(observations):
        obs_dict[o] = i
    return obs_dict

