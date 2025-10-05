#!/usr/bin/env python3

import sys
from operations import *


def check_option(option: str):
    if option != "-c":
        return False
    return True


def main(args=None):
    try:
        if args == None:
            args = sys.argv

        if len(args) < 3:
            raise Exception("Usage: ./main.py <option> <path_to_file>")

        file_path = args[2]
        option = args[1]

        if not check_option(option):
            raise Exception(f"ERROR - Incorrect option provided: {option}")

        res = count_nb_bytes(file_path, option)
        print(f"{res} {file_path}")
    except IsADirectoryError:
        print(f"ERROR - The provided path is a directory: {file_path}")
    except FileNotFoundError:
        print(f"ERROR - The provided file does not seem to exist: {file_path}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
