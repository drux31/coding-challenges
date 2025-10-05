# coding-challenges/ccwc/operations.py
import os


def count_nb_bytes(file_path: str, option: str):
    with open(file_path, "br") as f:
        content = f.read()
        return len(list(content))
