# A variable is visible only to statements inside the variable's scope
# A parameter variables scope is the func. in which the variable is used
# All of the statements inside the func. can access the parameter variable,
# But not outside the func. can access

## Making changes to parameters:
# When an argument passed to a func., the func. 
# parameter variable will reference the arguments value.
# However, any changes to the parameter variable will not affect the argument

def main():
    value = 99
    print('The value is ',value)
    changeMe(value)     #Funct call
    print('Back in main. The value is ', value)

def changeMe(x):
    print('I am changing the value.')
    x = 0
    print('Now the value is ', x)

main()
