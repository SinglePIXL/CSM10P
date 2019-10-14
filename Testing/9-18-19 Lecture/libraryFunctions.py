# Python like other programming languages comes with a 
# standard library functions that have already been written for us
# These functions are known as 'library functions'
# We have already used some of library functions like
# print, input, and range
# Some of python's lib. funcs. are built in the python interpreter
# like input print and range. We don't need to import anything to use them.

# Many function in the standard library are stored in
# files that are stored in modules.
# In roder to call a function that is stored in a module, we need
# to write an import statement.

import random

def main():
    for count in range(5):
        number = random.randint(1,70)
        print(number)

main()