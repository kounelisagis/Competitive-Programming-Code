from collections import defaultdict
from reader import *
import numpy as np


def find_demon_in_list(mylist, best_demon_index):
    for index, demon in enumerate(mylist):
        if demon[6] == best_demon_index:
            return index


def create_scores_dict():

    demons_score = defaultdict(int)
    demons_stamina_consumed_sorted = sorted(demons, key=lambda x: x[0])
    demons_total_score_sorted = sorted(demons, key=lambda x: x[5], reverse=True)
    demons_stamina_gained_sorted = sorted(demons, key=lambda x: x[2]/x[1], reverse=True)

    for index, demon in enumerate(demons_stamina_consumed_sorted):
        demons_score[demon[-1]] += D - index  # Give more points to the deamon with the lowest stamina needed

    for index, demon in enumerate(demons_total_score_sorted):
        demons_score[demon[-1]] += D - index  # Give more points to the deamon with the highest total fragment

    for index, demon in enumerate(demons_stamina_gained_sorted):
        demons_score[demon[-1]] += D - index  # Give more points to the deamon with the highest stamina gain

    return dict(sorted(demons_score.items(), key=lambda item: item[1], reverse=True))  # Retrun a sorted dict by value


if __name__ == "__main__":

    inputs = ['00-example', '01-the-cloud-abyss', '02-iot-island-of-terror', '03-etheryum', '04-the-desert-of-autonomous-machines', '05-androids-armageddon']
    
    # Repeat for each input file
    for input_file in inputs:
        filename = 'inputs/' + input_file + '.txt'
        Si, Smax, T, D, demons = read_input(filename)

        # preprocess
        for index, demon in enumerate(demons):
            # sum demons list
            demon.append( sum(demon[4][:min(T, len(demon[4]))]) )
            demon.append( index )

        output = []


        sorted_scores_dict = create_scores_dict()

        for demon_index in sorted_scores_dict:
            output.append(demon_index)  # Append the index of the demon to the output list. This index is the initial one given to the input


        # Assert that all ids in the output list are unique
        assert len(set(output)) == len(output)

        # Create the output file
        output_file = open('outputs/' + input_file + '_output.txt', 'w')
        output_file.write('\n'.join(map(str, output)))
        print(input_file + '.txt -> done')
