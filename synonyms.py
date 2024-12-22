'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 20, 2023.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as
    described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    base1 = 0
    base2 = 0
    top = 0

    for key, value in vec1.items():
        value1_sqr = value ** 2
        base1 += value1_sqr

    for key, value in vec2.items():
        value2_sqr = value ** 2
        base2 += value2_sqr

    for key1, value1 in vec1.items():
        for key2, value2 in vec2.items():
            if key1 == key2:
                mult = value1 * value2
                top += mult

    base = (base1 * base2)**(0.5)
    similarity = top/base

    return similarity


def build_semantic_descriptors(sentences):
    descriptors = {}

    for sentence in sentences:
        for word in sentence:
            descriptors[word] = {}

    for sentence in sentences:
        unique = set(sentence)
        for word in unique:
            for other_word in unique:
                if word != other_word:
                    descriptors[word][other_word] = descriptors[word].get(other_word, 0) + 1

    return descriptors


def build_semantic_descriptors_from_files(filenames):
    all_sentences = []

    for n in range(len(filenames)):
        file = open(filenames[n], "r", encoding="latin1")
        text = file.read()
        text = text.lower()
        text = text.replace("--", " ").replace(",", " ").replace("-", " ").replace(":", " ").replace(";", " ").replace("!", ".").replace("?", ".")
        sentences_inner = text.split(".")
        sentences_inner = [s.strip().split() for s in sentences_inner if s.strip()]

        for sentence in sentences_inner:
            all_sentences.append(sentence)

    descriptors = build_semantic_descriptors(all_sentences)
    return descriptors


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    max_similarity = -1
    best_choice = choices[0]

    for choice in choices:
        if word not in semantic_descriptors:
            similarity = -1
        elif choice not in semantic_descriptors:
            similarity = -1
        else:
            similarity = similarity_fn(semantic_descriptors[word], semantic_descriptors[choice])

        if similarity > max_similarity:
            max_similarity = similarity
            best_choice = choice

    return best_choice


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    total_count = 0
    correct_count = 0

    file = open(filename, "r", encoding="latin1")
    text = file.read()
    questions = text.split("\n")
    questions = [s.strip().split() for s in questions if s.strip()]

    for question in questions:
        word = question[0]
        correct = question[1]
        choices = question[2:]

        result = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
        if result == correct:
            correct_count += 1

        total_count += 1

    if total_count == 0:
        return 0.0
    amount_correct = correct_count / total_count
    percent_correct = amount_correct * 100

    return percent_correct


if __name__ == "__main__":
    L = 3