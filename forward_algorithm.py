
import numpy as np

def forward_algorithm(observation_sequence, prior_probability, transition_probabilities, emission_probabilities, observation_dict):

    observation_value = observation_dict[observation_sequence[0]]
    number_of_iterations = len(observation_sequence)
    alpha_value = np.multiply(np.transpose(emission_probabilities[:, observation_value]), prior_probability)

    for x in range(1, number_of_iterations):
        alpha_value = np.dot(alpha_value, transition_probabilities)
        observation_value = observation_dict[observation_sequence[x]]
        alpha_value = np.multiply(alpha_value, np.transpose(emission_probabilities[:, observation_value]))

    final_probability = alpha_value.sum()
    return final_probability
