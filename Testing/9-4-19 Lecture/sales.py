sales = float(input("enter amount of sales: "))
rate = float(input("Enter commission rate: "))
commission = sales * rate
print('The comission is $', format(commission, ',.2f', sep='' ))