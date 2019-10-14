# num = int(input('Enter your age')) # twenty three will give runtime error
# try runs code
# except runs code in case of error in try
# finally will exicute code reguardless of what happens in try or except
x = 20
try:
    #import theModule
    #print(x)
    #theModule.print()
    f = open('myfile.txt')
    f.write('Hello B')
except IOError:
    print('File cannot be found.')
except NameError:
    print("Variable 'x' is not defined.")
except ImportError:
    print('Module is not available')
except:
    print('Something else went wrong.')
else:
    print('There is no error.')
    x = x + 10
    print(x)

finally:
    print('We saved our files.')

try:
    print(y)
except NameError:
    print('y is not declared')

try:
    n1 = int(input('Enter first number for division: '))
    n2 = int(input('Enter second number for division: '))
    result = n1/n2
    print(result)

except ZeroDivisionError:
    print('You cannot divide by zero.')

finally:
    print('I like python')