flag = 'y'
total = 0.0
while flag == 'y':
    sales = float(input('Enter a sale value: '))
    total = total + sales
    flag = input('Enter y to continue or enter N to stop: ')
print('Total sales is:', total)