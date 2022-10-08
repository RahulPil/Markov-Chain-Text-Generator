import random


def read_file(file):
    return open(file, 'r', encoding="utf8").read()


def generate_transition_matrix(file, k):
    words_in_file = file.split()
    markov_transition_matrix = {}

    for i in range(len(words_in_file) - k):
        current_state = " ".join(tuple(words_in_file[i:i + k]))
        next_state = " ".join(tuple(words_in_file[i + k:i + (2 * k)]))

        if markov_transition_matrix.get(current_state) is None:
            markov_transition_matrix[current_state] = {}
            markov_transition_matrix[current_state][next_state] = 1
        else:
            if markov_transition_matrix[current_state].get(next_state) is None:
                markov_transition_matrix[current_state][next_state] = 1
            else:
                markov_transition_matrix[current_state][next_state] += 1

    for curr_state, transition in markov_transition_matrix.items():
        total_freq = sum(transition.values())
        for state, freq in transition.items():
            markov_transition_matrix[curr_state][state] = freq / total_freq

    return markov_transition_matrix


def generate_sentences(markov_transition_matrix, starting_words, limit):
    generated_words = starting_words + " "
    current_state = starting_words

    for i in range(limit - 1):
        next_state = random.choices(list(markov_transition_matrix[current_state].keys()),
                                    list(markov_transition_matrix[current_state].values()))
        current_state = next_state[0]
        generated_words += current_state + " "

    return generated_words
