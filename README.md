# PY4E_Mod_11_1_Python_grep
Grep python implementation

## Directions
Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression. 

The file, named mbox-long.txt is included in this repo.  You will need to do the implementation to open and read through the file in your program.

## Starter Code
```python
import re

def count_pattern_in_file():
    regular_expression = input("Enter a regular expression: ")


if __name__ == '__main__':
    count_pattern_in_file()
```

## Expected Output
```
Enter a regular expression: ^Author 
mbox.txt had 1798 lines that matched ^Author
```
## Testing

To test your program use pytest

`pytest`

`python -m pytest`

(Python should be able to find the test file on its own)
