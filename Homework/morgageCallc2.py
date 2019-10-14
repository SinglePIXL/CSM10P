# Alec
# morgageCalc2.py
# 10-12-19
# Ver 1.8
# A program that gets the principal, rate, and term of a morgage
# and outputs the monthly payment. Uses try and except for input validation.

def main():
    prin = int(principalInput())
    rate = float(rateInput())
    term = int(termInput())
    rate = rate / 1200
    term = term * 12
    mpay = (prin * rate)/(1-(rate + 1)**(-term))
    print('Your monthly morgage payment is $' + format(mpay,',.2f',\
         ),'per month.')

def principalInput():
    # If invalid input, ask again for principal
    while True:
        try:
            principal = int(input('Enter your principal: '))
            # Input validation
            assert int(principal)>0
            assert int(principal)>5000
            assert int(principal)<1000000
            # Exit loop and return principal
            break
        # Catch assertion errors
        except AssertionError:
            print('Assertion error: Principal must not be negative',
            'and must be between 5,000 and 1,000,000.')
        # Catch ValueErrors
        except ValueError:
            print('You entered a string')
        
    return principal

def rateInput():
    # If invalid input, ask again for rate
    while True:
        try:
            rate = float(input('Enter your morgage rate: '))
            # Input validation
            assert float(rate)>0
            assert float(rate)>3.25
            assert float(rate)<6.25
            # Exit loop and return rate
            break
        # Catch assertion errors
        except AssertionError:
            return 'Rate must not be negative and be between 3.25 and 6.25'
        # Catch ValueErrors
        except ValueError:
            print('You entered a string')
        
    return rate

def termInput():
    # If invalid input, ask again for
    while True:
        try:
            term = int(input('Enter your term: '))
            # Input validation
            assert int(term)>0
            assert int(term)>10
            assert int(term)<40
            # Exit loop and return term
            break
        # Catch assertion errors
        except AssertionError:
            return 'Term must not be negative and be between 10 and 40.'
        # Catch ValueErrors
        except ValueError:
            print('You entered a string.')
      
    return term

main()