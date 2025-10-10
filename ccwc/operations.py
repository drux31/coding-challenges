# coding-challenges/ccwc/operations.py
import os

def get_file(file_path):
    f = open(file_path, "rb")
    return f

def count_nb_bytes(file):
    return len(list(file.read()))


def count_nb_lines(file):
    return sum(1 for line in file)

def count_nb_words(file_path):
    with open(file_path, "rb") as f:
        return 
    
def run_op(file_path, option=None):
    file = get_file(file_path)
    res = None
    match option:
        case "-c":
            res = count_nb_bytes(file)
        case "-l":
            res = count_nb_lines(file)
    file.close()
    return res
            