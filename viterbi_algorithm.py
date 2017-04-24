import numpy as np


def viterbi(states, observations, start_probability, transition_probability, emission_probability, obs_map, state_map):
    observation_value = obs_map[observations[0]]
    delta_value = np.multiply(np.transpose(emission_probability[:, observation_value]), start_probability)

    number_of_states = len(states)
    number_of_iterations = len(observations)
    next_path = np.zeros((number_of_iterations, number_of_states))
    prev_path = np.zeros((number_of_iterations, number_of_states))
    delta_value = delta_value / np.sum(delta_value)
    prev_path[0, :] = [i for i in range(number_of_states)]

    for x in range(1, number_of_iterations):
        observation_value = obs_map[observations[x]]
        temp = np.multiply(np.multiply(delta_value, transition_probability.transpose()),
                           emission_probability[:, observation_value])
        delta_value = temp.max(axis=1).transpose()
        delta_value = delta_value / np.sum(delta_value)
        argmax = temp.argmax(axis=1).transpose()
        argmax = np.ravel(argmax).tolist()
        for s in range(number_of_states):
            next_path[:x, s] = prev_path[0:x, argmax[s]]
        next_path[x, :] = [i for i in range(number_of_states)]
        prev_path = next_path.copy()

    final_value = np.argmax(np.ravel(delta_value))
    final_path = prev_path[:, final_value].tolist()
    final_state_sequence = [state_map[i] for i in final_path]
    return final_state_sequence
