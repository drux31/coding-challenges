import pytest
from operations import *

FILE_PATH = "resources/edmag.txt"

def open_file():
    return open(FILE_PATH, "rb")

def test_count_nb_bytes():
    file = open_file()
    assert count_nb_bytes(file) == 593788
    file.close


def test_count_nb_lines():
    file = open_file()
    assert count_nb_lines(file) == 9873
    file.close
