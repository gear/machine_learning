__author__ = 'naveed'

# Takes a dataset and a character list as input and outputs a vector representation
def vectorize(data_list, char_list, empty_vector):
    data_vector = [];
    for input in data_list:
        word_vector = [];
        for character in input:
            char_vector = list(empty_vector);
            if character in char_list:
                position = char_list.index(character);
                char_vector[position] = 1.0;
            word_vector = word_vector + char_vector;
        data_vector.append(word_vector);
    return data_vector;
