def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print('division by zero')
    else:
        print('The result is,', result)
    finally:
        print('Executing finally block.')

def main():
    x = int(input('Number1: '))
    y = int(input('Number2: '))
    divide(x,y)

main()