def getName():
    first = input('Enter first name: ')
    last = input('Enter last name: ')
    return first,last

def main():
    fname,lname = getName()
    print('The full name is:', fname, lname)

main()