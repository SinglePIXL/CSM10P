def determine_total_Grade(average):
    if average <= 100 and average >= 90:
        print('Your average of ', average, 'is an A!')
    
    elif average <= 89 and average >= 80:
        print('Your average of ', average, 'is a B.')

    elif average <= 79 and average >= 70:
        print('Your average of ', average, 'is a C')

    elif average <= 69 and average >= 70:
        print('Your average of ', average, 'is a D')

    else:
        print('Your average of ', average, 'is an F')