import pytest
from main import main


def test_main_count_bytes(capsys):
    test_case = ["main", "-c", "resources/edmag.txt"]

    # test case with the correct for counting bytes
    main(test_case)
    captured = capsys.readouterr()
    assert captured.out.strip() == "593788 resources/edmag.txt"


def test_main_count_lines(capsys):
    test_case = ["main", "-l", "resources/edmag.txt"]

    # test case with the correct output for counting bytes
    main(test_case)
    captured = capsys.readouterr()
    assert captured.out.strip() == "9873 resources/edmag.txt"


def test_main_count_words(capsys):
    test_case = ["main", "-w", "resources/edmag.txt"]

    # test case with the correct output for counting words
    main(test_case)
    captured = capsys.readouterr()
    assert captured.out.strip() == "97235 resources/edmag.txt"


def test_main_incorrect_option():
    test_case = ["main", "-v", "resources/edmag.txt"]

    # test case with the incorrect option
    with pytest.raises(Exception) as exinfo:
        main(test_case)
    assert f"ERROR - Incorrect option provided: {test_case[1]}" in str(exinfo.value)


def test_main_with_directory(capsys):
    test_case = ["main", "-c", "resources/"]

    # test case with a directory
    main(test_case)
    captured = capsys.readouterr()
    assert (
        captured.out.strip()
        == f"ERROR - The provided path is a directory: {test_case[2]}"
    )


def test_main_inexisting_file(capsys):
    test_case = ["main", "-c", "resources/iso.txt"]

    # test case with a file that does not exist
    main(test_case)
    captured = capsys.readouterr()
    assert (
        captured.out.strip()
        == f"ERROR - The provided file does not seem to exist: {test_case[2]}"
    )
