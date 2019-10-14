salary = 0.01
days = int(input('Enter number of days'))
if days > 64 or days =< 0:
    print('Please choose a number greater than 0 or equal or less than 64')

else:
    for num in range (1, days + 1):
        print(num)