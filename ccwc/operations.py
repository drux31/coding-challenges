# coding-challenges/ccwc/operations.py
import os

def get_file(file_path):
    f = open(file_path, "rb")
    return f

def count_nb_bytes(file):
    return len(list(file.read()))


def count_nb_lines(file_path):

    with open(file_path, "rb") as f:
        num_lines = sum(1 for line in f)
        return num_lines

def count_nb_words(file_path):
    with open(file_path, "rb") as f:
        return 
    
def run_op(file_path, option=None):
    file = get_file(file_path)
    res = None
    match option:
        case "-c":
            res = count_nb_bytes(file)
    file.close()
    return res
            