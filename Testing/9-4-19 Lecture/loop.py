flag = 'Y'      # initialization
while flag == 'Y':
    sales = float(input('Enter amount of sales:'))
    rate = float(input('Enter comission rate:'))
    comission = sales * rate
    print('The comission is $', format(comission, ',.2f'), sep='')
    flag = input(' Do you want to calculate another comission? Enter Y/n:')