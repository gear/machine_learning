__author__ = 'naveed';

import input;
import model;
import numpy

file_name = input.read_file();
csv_list = input.list_converter(file_name);


name_list = [i[1] for i in csv_list];
stat_list = [i[2] for i in csv_list];

WORD_LENGTH = 5;
VECTOR_SIZE = 80;

training_examples = len(name_list);
feature_count = WORD_LENGTH * VECTOR_SIZE;
empty_vector = list(numpy.zeros(VECTOR_SIZE));

# Splitting name list and converting to unicode
name_list_split =  [i.split(';') for i in name_list];
name_list_dec = [[value[2:] for value in row] for row in name_list_split];
name_list_hex = [[hex(int(value)) for value in row] for row in name_list_dec];
name_list_uni = [[unichr(int(value)) for value in row] for row in name_list_dec];

# Truncating names and adding whitespace to make length equal 5
for i in name_list_uni:
    while len(i)<5:
        i.append(u' ');
    if len(i)>5:
        del i[5:];

# Reading list of katakana characters in unicode format
kat_list = input.kat_convert('data/katakana');

data_vector = model.vectorize(name_list_uni,kat_list,empty_vector);
