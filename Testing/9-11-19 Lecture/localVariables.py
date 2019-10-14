def main():
    firstName = getName()
    print( 'Hello', firstName )

def getName():
    name = input('Enter your name')
    return name

main()