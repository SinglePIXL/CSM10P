# The order of the keyword arguments does not match the order of parameters
# in the function header.
# Because a keyword argument specifies which parameter the argument should 
# be passed into, it's position in the func. call does not matter

showInterest(rate=0.01, periods=10, principal=10000.0)

def showInterest(principal, rate, periods):
    interest = principal * rate * periods
    print('The simple interest is: ', format(interest,',.2f'))
