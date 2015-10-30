__author__ = 'naveed';

# This module contains function for reading and converting datasets

import csv;
import sys;

# Reads the command line arguments and returns the file name
def read_file():
    input_file = sys.argv[1];
    file_path = 'data/' + input_file;
    return file_path;

# Takes as input a csv file object, and returns a list of elements
def list_converter(filename='data/machine_learning.csv'):
    open_file = open(filename, 'rb');
    data_csv = csv.reader(open_file, delimiter=',');
    list_csv = [];
    for i in data_csv:
        list_csv.append(i);
    return list_csv;

# Reads a file containing newline separated katakana characters and converts to unicode
def kat_convert(filename='data/katakana'):
    file_kat = open(filename, 'r');
    kat = file_kat.read();
    kat_list = kat.split('\n');
    uni_list = [unicode(i, 'utf-8') for i in kat_list];
    return uni_list;
