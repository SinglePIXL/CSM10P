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
    principal = int(input('Enter your principal: '))
    # GIGO invaliid inputs
    while principal < 100000 or principal > 1000000:
        principal = int(input('Please choose a valid number within the'
            ' range of 100,000 and 1,000,000: '))
    # Get rate from user
    rate = float(input('Enter your morgage rate: '))
    # GIGO invalid numbers
    while rate < 0:
        rate = float(input('Please choose a valid number greater than 0: '))
    # Get term from user
    term = int(input('Enter your term length: '))
    # GIGO invalid numbers
    while term < 0:
        term = int(input('Please choose a valid number greater than 0: '))
    
    return principal,rate,term

# Perform math using the values provided from the user and output the result
def main():
    prin,rate,term = paymentParams()
    rate = rate / 1200
    term = term * 12
    mpay = (prin * rate)/(1-(rate + 1)**(-term))
    print('Your monthly morgage payment is $' +format(mpay,',.2f',\
         ),'per month.')

main()

