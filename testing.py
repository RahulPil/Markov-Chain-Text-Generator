from markov_chain_text_generator import *

if __name__ == "__main__":
    file = read_file("test_file.txt")
    markov_model = generate_transition_matrix(file, 2)
    story = generate_sentences(markov_model, "he thought", 100)

    print(story)
