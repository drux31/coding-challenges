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
================================================= test session starts =========================================================
platform linux -- Python 3.10.12, pytest-8.4.2, pluggy-1.6.0
rootdir: /home/drux/projects/coding-challenges/ccwc
configfile: pyproject.toml
collected 5 items

test_main.py ....                                                                                                         [ 80%]
test_operations.py .                                                                                                      [100%]

================================================== 5 passed in 0.03s ===========================================================

```

### Step two - number of lines in a file

##### Implementation

In this step, the goal is to support the command line option -l that outputs the number of lines in a file :

```
> ccwc -l resources/test.txt
7145 resources/test.txt
```

##### Tests with pytest

Tests results should look like this:

```
========================================================= test session starts ========================================================
platform linux -- Python 3.10.12, pytest-8.4.2, pluggy-1.6.0
rootdir: /home/drux/projects/coding-challenges/ccwc
configfile: pyproject.toml
collected 7 items

test_main. .....                                                                                                                [ 71%]
test_operations.py ..                                                                                                           [100%]

=========================================================== 7 passed in 0.04s ========================================================
```

### Step three - number of words in a file

##### Implementation

In this step our goal is to support the command line option -w that outputs the number of words in a given file:

```
>ccwc -w resources/test.txt
   58164 resources/test.txt
```

##### Tests with pytest

Tests results should look like this:

```
========================================================= test session starts ========================================================
platform linux -- Python 3.10.12, pytest-8.4.2, pluggy-1.6.0
rootdir: /home/drux/projects/coding-challenges/ccwc
configfile: pyproject.toml
collected 9 items

test_main. .....                                                                                                                [ 66%]
test_operations.py ..                                                                                                           [100%]

=========================================================== 9 passed in 0.05s ========================================================
```

### Step four - number of characters in a file

##### Implementation

In this step our goal is tto support the command line option -m that outputs the number of characters in a given file:

```
>wc -m resources/test.txt
  339292 resources/test.txt

>ccwc -m resources/test.txt
  339292 resources/test.txt
```

**Note**: If the current locale does not support multibyte characters, this will match the -c option.

##### Tests with pytest

Tests results should look like this:

```
========================================================= test session starts ========================================================
platform linux -- Python 3.10.12, pytest-8.4.2, pluggy-1.6.0
rootdir: /home/drux/projects/coding-challenges/ccwc
configfile: pyproject.toml
collected 11 items

test_main. .....                                                                                                                [ 63%]
test_operations.py ..                                                                                                           [100%]

=========================================================== 11 passed in 0.05s ========================================================
```

### Step five - default behaviour

##### Implementation

In this step our goal is to support the default option - i.e. no options are provided, which is the equivalent to the -c, -l and -w options:

```
>ccwc resources/test.txt
  7145   58164  342190 resource/test.txt
```

**Note**: If the current locale does not support multibyte characters, this will match the -c option.

##### Tests with pytest

Tests results should look like this:

```
========================================================= test session starts ========================================================
platform linux -- Python 3.10.12, pytest-8.4.2, pluggy-1.6.0
rootdir: /home/drux/projects/coding-challenges/ccwc
configfile: pyproject.toml
collected 11 items

test_main. .....                                                                                                                [ 63%]
test_operations.py ..                                                                                                           [100%]

=========================================================== 11 passed in 0.05s ========================================================
```
