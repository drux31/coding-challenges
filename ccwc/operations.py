# coding-challenges/ccwc/operations.py
import os

def get_file(file_path):
    f = open(file_path, "rb")
    return f

def count_nb_bytes(file):
    return len(list(file.read()))


def count_nb_lines(file):
    return sum(1 for line in file)

def count_nb_words(file):
    return len(file.read().split())
    
def run_op(file_path, option=None):
    file = get_file(file_path)
    res = None
    match option:
        case "-c":
            res = count_nb_bytes(file)
        case "-l":
            res = count_nb_lines(file)
        case "-w":
            res = count_nb_words(file)

    file.close()
    return res
            