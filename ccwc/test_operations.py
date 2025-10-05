import pytest
from operations import *

FILE_PATH = "resources/edmag.txt"


def test_count_nb_bytes():
    assert count_nb_bytes(FILE_PATH) == 593788


def test_count_nb_lines():
    assert count_nb_lines(FILE_PATH) == 9873
