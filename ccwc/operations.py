# coding-challenges/ccwc/operations.py
import os


def count_nb_bytes(file_path: str):
    with open(file_path, "br") as f:
        content = f.read()
        return len(list(content))


def count_nb_lines(file_path):
    with open(file_path, "rb") as f:
        num_lines = sum(1 for line in f)
        return num_lines
