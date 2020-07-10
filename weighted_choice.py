from random import random


def choose_value(options):
    # adapted from: https://scriptinghelpers.org/questions/11242/how-to-make-a-weighted-selection
    for i in range(len(options)):
        options[i]['weight'] += 1
        # Make everything more likely to be picked
        # (accumulates between random choices)

    # -- Sum all weights
    total_weight = sum([o['weight'] for o in options])

    # -- Pick random value
    rand = random() * total_weight
    choice = None

    # -- Search for the interval [0, w1] [w1, w1 + w2] [w1 + w2, w1 + w2 + w3 ] ....
    # -- that `rand` belongs to
    # -- and select the corresponding choice
    for i, option in enumerate(options):
        if rand < option['weight']:
            choice = options[i]['song']
            option['weight'] = 1  # Reset weight to small value
            break
        else:
            rand -= option['weight']

    return choice


if __name__ == '__main__':

    choices = [
        {'color': "Red", 'weight': 1},
        {'color': "Blue", 'weight': 1},
        {'color': "Yellow", 'weight': 1},
        {'color': 'Green', 'weight': 1}]

    for x in range(10):
        print(choose_value(choices))
        for item in choices:
            print(item['color'], item['weight'], end=' ')
        print('\n')
