#!/usr/bin/env python3

import sys
from operations import *
from constants import *


def check_option(option: str):
    if not option in OPTIONS:
        return False
    return True


def main(args=None):
    try:
        if args == None:
            args = sys.argv

        if len(args) == 2 and not check_option(args[1]):
            file_path = args[1]
            nb_lines, nb_words, nb_bytes = run_op(file_path)
            print(f"{nb_lines} {nb_words} {nb_bytes} {file_path}")
        elif (len(args) == 2 and check_option(args[1])) and not sys.stdin.isatty():
            file_path = sys.stdin
            res = run_op(file_path, args[1])
        elif len(args) == 1 and not sys.stdin.isatty():
            file_path = sys.stdin
            print(file_path)
            nb_lines, nb_words, nb_bytes = run_op(file_path)
            print(f"{nb_lines} {nb_words} {nb_bytes} {file_path}")
        elif len(args) == 3:
            file_path = args[2]
            option = args[1]
            if not check_option(option):
                raise Exception(f"ERROR - Incorrect option provided: {option}")
            res = run_op(file_path, option)
            if res != None:
                print(f"{res} {file_path}")
        else:
            raise Exception("Usage: ccwc [option] <path_to_file>")

    except IsADirectoryError:
        print(f"ERROR - The provided path is a directory: {file_path}")
    except FileNotFoundError:
        print(f"ERROR - The provided file does not seem to exist: {file_path}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
