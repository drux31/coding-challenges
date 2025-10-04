# coding-challenges/ccwc/operations.py
import os

def check_file(file_path: str):
    if not os.path.exists:
        raise FileExistsError(f"No such file: {file_path}")
    elif not os.path.isfile:
        raise IsADirectoryError(f"{file_path} is not a simple file!")
    
def check_option(option: str):
    if option != "-c":
        raise Exception(f"Incorrect option provided {option}")
    return True

def count_nb_bytes(file_path: str, option: str):
    try:
        check_file(file_path)
        if check_option(option):
            with open(file_path, "br") as f:
                content = f.read()
                return len(list(content))
    except Exception as e:
        return e
    except IsADirectoryError :
        return f"{file_path} is not a simple file!"
    except FileNotFoundError as e:
        return e