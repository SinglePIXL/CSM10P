# IOError: if the file cannot be opened.

# ImportError: if python cannot find the module.

# ValueError: Raised when a built in operation or function recieves an argument
# that has the right type but an inapropriate value

# KeyboardInterrupt: Raised when the user hits the interrupt key

# EOFError: Raised one of the builtin functions (like input()) hits an end
# of file condition (EOF) without reading any 

# forty = ValueError

# Using "assert" statement ou ca initially create your own exception
# assert statement checks for a condition. If the condition is not met(false)
# then it will throw exception error.
def input_age(age):
    try:
        assert int(age)>18
    except ValueError:
        return 'ValueError: cannot convert to int'
    else:
        return 'Age is saved succesfully.'
        

def main():
    age = int(input('Enter your age'))
    print(input_age(age))
    print(input_age('23'))
    print(input_age(25))
    print(input_age('nothing'))

main()