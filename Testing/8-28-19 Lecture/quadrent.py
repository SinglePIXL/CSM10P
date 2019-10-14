x = int(input('Enter a value'))
y = int(input('Enter a value'))
if x>0:
    if y>0:
        print('Point is in I quad.')
    else:
        print('Pint is in IV quad')

else:
    if y>0:
        print('Point is in II quad')
    else:
        print('Point is in III quad')