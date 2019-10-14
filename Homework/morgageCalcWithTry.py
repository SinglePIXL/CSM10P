# Alec
# morgageCalc.py
# 9-29-19
# Ver 1.7
# 
# A program that uses two functions. One to get the principal, rate, and term
# of a morgage payment, and another to calculate the monthly payment. 
# No global variables.

# Function to get values from the user and ignore invalid inputs
def paymentParams():
    # Get the principal from the user
    while True:
        try:
            principal = int(input('Enter your principal: '))
            assert int(principal)>0#, 'Principal must not be negative'
            assert int(principal)>5000#, 'Principal must be greater than 5,000'
            assert int(principal)<1000000#, 'Principal must be less than 1,000,000'
            break
        # GIGO invaliid inputs
        except AssertionError:
            print('Assertion error: Principal must not be negative',
            'and must be between 5,000 and 1,000,000.')
    # Get rate from user
    while True:
        try:
            rate = float(input('Enter your morgage rate: '))
            assert int(rate)>0
            assert int(rate)<3.25
            assert int(rate)>6.25
            break
        except AssertionError:
            return 'Rate must not be negative and be between 3.25 and 6.25'
        
    while True:
        try:
            term = int(input('Enter your term: '))
            assert int(term)>0
            assert int(term)<10
            assert int(term)>40
            break
        except AssertionError:
            return 'Term must not be negative and be between 10 and 40.'

    
    return principal,rate,term

# Perform math using the values provided from the user and output the result
def main():
    while True:
        try:
            prin,rate,term = paymentParams()
        except ValueError:
            return 'ValueError'
        else:
            break
    # prin = paymentParams()
    # rate = paymentParams()
    # term = paymentParams()
    rate = rate / 1200
    term = term * 12
    mpay = (prin * rate)/(1-(rate + 1)**(-term))
    print('Your monthly morgage payment is $' +format(mpay,',.2f',\
         ),'per month.')

main()

