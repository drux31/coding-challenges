# coding-challenges/ccwc/operations.py
import os
from functools import reduce


def get_file(file_path):
    f = open(file_path, "rb")
    return f


def count_nb_bytes(file):
    return len(list(file.read()))


def count_nb_lines(file):
    return sum(1 for line in file)


def count_nb_words(file):
    return len(file.read().split())


def count_nb_characters(file):
    text = file.read()
    return len(text.decode("utf8"))


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
        case "-m":
            res = count_nb_characters(file)
        case _:
            file1 = get_file(file_path)
            file2 = get_file(file_path)
            file3 = get_file(file_path)
            a = count_nb_lines(file1)
            b = count_nb_words(file2)
            c = count_nb_bytes(file3)
            file1.close()
            file2.close()
            file3.close()
            res = (a, b, c)
            # return (count_nb_lines(file), count_nb_words(file), count_nb_bytes(file))
    file.close()
    return res
