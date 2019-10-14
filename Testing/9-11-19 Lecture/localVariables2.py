def main():
    value = int(input('Enter an integer number: '))
    showDouble(value)   # Argument in func. call
    print('Yay!')

def showDouble(number): # Paramiter
    result = number * 2
    print(result)

main()