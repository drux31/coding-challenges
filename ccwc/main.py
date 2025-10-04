#!/usr/bin/env python3

import sys
import os
from read_file import *


def main():
    args = sys.argv
    if len(args) < 3:
        print("Missing argument!")
        print("Expected: ccwc -c file_path")
        sys.exit(1)

    file_path = args[2]
    option = args[1]
    res = read_file(file_path, option)
    print(f"{res} {file_path}")


if __name__ == "__main__":
    main()
