# There are no global constants in python 
# But we can use global variables and declare those as UPPERCASE without
# using "global" keyword in front of it within anywhere in the program.

PI = 3.14
def main():
    radius = float(input('Enter radius of a circle: '))
    area = PI * radius * radius
    showValue(area)

def showValue(area):
    print('The PI is ', PI)
    print(area)

main()