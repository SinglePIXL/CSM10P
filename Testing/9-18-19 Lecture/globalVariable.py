# If we want a statement in a function to assign a value to a global variable, we must 
# declare the global variable using keyword "global"
#
# We should restrict or not use global global variables at all
# Global variables makes debugging difficult
# Functions using globals are usually dependant on those variables
# 



number = 0 
def main():
    global number       # number can be seen in any function
    number = int(input('Enter a number: '))
    show_number()
    stupidFunction()

def show_number():
    print('The number you entered is ', number)

def stupidFunction():
    print(number)
main()