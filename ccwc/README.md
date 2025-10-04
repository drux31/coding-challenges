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

in the third case, you'll have to create an alias in your system (like alias **ccwc='uv run main.py'**).

### step one - simple version

The goal is to write a simple version of wc takes a command line option -c, and ouputs the number of bytes in a given file. Example with our test.txt file:

```
> ccwc -c test.txt
  342190 test.txt
```
