def main():
    
    # Ask the user how many days they worked.
    ndays = int(input('Enter the number of days worked: '))
    pay = 0.005 # my starting salary
    
    # Create the function to calculate the pay per day.
    for day in range(1,ndays+1):
        #pay = pay * 2.0
        pay *= 2.0
        print(' Day', day, ' Salary', pay)

    # State the results of the function.
    print('Your salary on day', ndays, 'would be $%.2f' % pay)

# Call the main function.
main()