import pytest
from operations import count_nb_bytes

def test_count_nb_bytes():
    file_path = "resources/file1.txt"
    option1 = "-c"
    option2 = "-v"

    assert count_nb_bytes(file_path, option1) == 593788
    assert count_nb_bytes(file_path, option2) == f"Incorrect option provided {option2}"
    
