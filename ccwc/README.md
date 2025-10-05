## wc Tool

This challenge is to build our own version of the Unix command line tool wc.
The final solution will counting words, lines, characters and bytes from a given file.

This version is built using python, the file used for testing purposes is the test.txt file in the project folder.

### Running the program

To run the program, you can use one of the following command:

```
> uv run main.py **option** **file_path**
or
> ./main.py **option** **file_path**
or
> ccwc **option** **file_path**
```

in the third case, you'll have to create an alias in your system (like **alias ccwc='uv run main.py'**).

### Step one - simple version

##### implementation

The goal is to write a simple version of wc takes a command line option -c, and ouputs the number of bytes in a given file. Example with our test.txt file:

```
> ccwc -c resources/test.txt
  342190 resources/test.txt
```

##### Tests with pytest

We created test files to make sure our tool behaves accordingly. The test files are placed in the root directory of the project for convenience, so we can avoid having pytest not finding the project module. We have five cases tested.

```
> uv run pytest
===================================================================== test session starts ======================================================================
platform linux -- Python 3.10.12, pytest-8.4.2, pluggy-1.6.0
rootdir: /home/drux/projects/coding-challenges/ccwc
configfile: pyproject.toml
collected 5 items

test_main.py ....                                                                                                                                         [ 80%]
test_operations.py .                                                                                                                                      [100%]

====================================================================== 5 passed in 0.03s =======================================================================

```

### Step two - number of lines in a file

##### Implementation

In this step, the goal is to support the command line option -l that outputs the number of lines in a file :

```
> ccwc -l resources/test.txt
7145 resources/test.txt
```
