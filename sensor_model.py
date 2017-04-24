import numpy as np

states = ('s1', 's2', 's3')

possible_observations = ('0', '1', '2')

observation_sequence = (
    '0', '0', '0', '2', '0', '1', '2', '0', '0', '2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '2',
    '1', '1', '0', '2', '1', '1', '0', '2', '1', '1')

prior_probability = np.matrix('1 0 0')

transition_probabilities = np.matrix([[0.9411, 0.02941, 0.02941],
                                      [0.2, 0.8, 0],
                                      [0.2, 0, 0.8]])

emission_probabilities = np.matrix([[0.375, 0.375, 0.25],
                                    [0, 1, 0],
                                    [1, 0, 0]])


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
    state_map = {}
    for i, o in enumerate(states):
        state_map[i] = o
    return state_map


def get_observation_dict(observations):
    obs_map = {}
    for i, o in enumerate(observations):
        obs_map[o] = i
    return obs_map
