def is_even(number):
    if(number%2==0):
        status = True

    else:
        status = False

    return status

def main():
    number = int(input('Enter a number: '))
    if is_even(number):
        print('This number is even')

    else:
        print('This number is odd')

main()