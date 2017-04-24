import casino1_model
import casino2_model
import forward_algorithm
import viterbi_algorithm
import sensor_model

def main():

    print("--PROBLEM3-_FORWARD ALGORITHM___")
    print
    ## Casino 1 forward algorithm
    prior_probability1 = casino1_model.get_prior_probabilty()
    states1 = casino1_model.get_states()
    possible_observations1 = casino1_model.get_possible_observations()
    observation_sequence1 = casino1_model.get_observation_sequence()
    transition_probabilities1 = casino1_model.get_transition_probabilties()
    emission_probabilities1 = casino1_model.get_emission_probabilities()
    observation_dict1 = casino1_model.get_observation_dict(possible_observations1)
    state_dict1 = casino1_model.get_state_dict(states1)
    casino1_final_probability = forward_algorithm.forward_algorithm(observation_sequence1, prior_probability1, transition_probabilities1, emission_probabilities1, observation_dict1)
    print("Likelihood of Casino1: {}".format(casino1_final_probability))

    ## Casino 2 forward algorithm
    prior_probability2 = casino2_model.get_prior_probabilty()
    states2 = casino2_model.get_states()
    possible_observations2 = casino2_model.get_possible_observations()
    observation_sequence2 = casino2_model.get_observation_sequence()
    transition_probabilities2 = casino2_model.get_transition_probabilties()
    emission_probabilities2 = casino2_model.get_emission_probabilities()
    observation_dict2 = casino2_model.get_observation_dict(possible_observations2)
    state_dict2 = casino2_model.get_state_dict(states2)
    casino2_final_probability = forward_algorithm.forward_algorithm(observation_sequence2, prior_probability2,
                                                                    transition_probabilities2,
                                                                    emission_probabilities2, observation_dict2)
    print("Likelihood of Casino2: {}".format(casino2_final_probability))

    if casino1_final_probability > casino2_final_probability:
        print("Casino1 is more likely")
    else:
        print("Casino2 is more likely")
    print
    print("--PROBLEM3-VITERBI ALGORITHM___")
    print
    casino2_path = viterbi_algorithm.viterbi(states2, observation_sequence2, prior_probability2, transition_probabilities2, emission_probabilities2,
                                             observation_dict2, state_dict2)
    print(casino2_path)

    prior_probability3 = sensor_model.get_prior_probabilty()
    states3 = sensor_model.get_states()
    possible_observations3 = sensor_model.get_possible_observations()
    observation_sequence3 = sensor_model.get_observation_sequence()
    transition_probabilities3 = sensor_model.get_transition_probabilties()
    emission_probabilities3 = sensor_model.get_emission_probabilities()
    observation_dict3 = sensor_model.get_observation_dict(possible_observations3)
    state_dict3 = sensor_model.get_state_dict(states3)
    sensor_path = viterbi_algorithm.viterbi(states3, observation_sequence3, prior_probability3, transition_probabilities3, emission_probabilities3,
                                             observation_dict3, state_dict3)
    print
    print("--PROBLEM4-VITERBI ALGORITHM___")
    print
    print(sensor_path)

if __name__ == "__main__":
    main()
