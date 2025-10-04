import os
import sys


def read_file(file_path: str, option: str):
    if option == "-c":
        with open(file_path, "br") as f:
            content = f.read()
            return len(list(content))
    else:
        return f"Incorrect option provided {option}"
