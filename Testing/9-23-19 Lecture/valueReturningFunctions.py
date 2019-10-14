def sum(num1, num2):    # Function header (parameters)
    total = num1 + num2
    return total

def main():
    n1 = int(input('Enter the first number: '))
    n2 = int(input('Enter the second number: '))

    result = sum(n1,n2)     # Function Call
    print('The total is:', result)


main()