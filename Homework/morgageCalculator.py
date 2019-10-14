def paymentParams(p,r,t):
    p = int(input('Enter your principal: '))
    while p < 100000 or p > 1000000:
        p = int(input('Please choose a valid number within the range of \
            100,000 and 1,000,000: '))

    r = float(input('Enter your morgage rate: '))
    while r < 0:
        r = float(input('Please choose a valid number greater than 0: '))
    t = int(input('Enter your term length: '))
    while t < 0:
        t = int(input('Please choose a valid number greater than 0: '))
    
    return p,r,t

def morgMath():
    prin = 0
    rate = 0
    term = 0
    prin,rate,term = paymentParams(prin,rate,term)
    rate = rate / 1200
    term = term * 12
    mpay = (prin * rate)/(1-(rate + 1)**(-term))
    print('Your monthly morgage payment is ', '$',format(mpay,',.2f'),end='')

morgMath()

