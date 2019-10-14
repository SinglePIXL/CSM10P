# The order of the keyword arguments does not match the order of parameters
# in the function header.
# Because a keyword argument specifies which parameter the argument should 
# be passed into, it's position in the func. call does not matter

def main():
    fName = input('Enter your first name: ')
    lName = input('Enter your last name: ')
    print('Your name reversed is ')
    reverseName(last=lName, first=fName)
def reverseName(first, last):
    print(last, first)

main()