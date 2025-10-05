import pytest
from operations import count_nb_bytes


def test_count_nb_bytes():
    file_path = "resources/edmag.txt"
    option1 = "-c"

    assert count_nb_bytes(file_path, option1) == 593788
