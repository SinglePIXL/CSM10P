# Alec
# randomNumbersReadWrite.py
# 10-2-19
# Ver 2.1

# A program that writes a series of random numbers to a file.
# Each random number should be in the range of 1 through 100.
# The user specifies how many random numbers the file will hold.

import random

def main():
    outfile = open('randomNumbers.txt','w')
    # Ask user for number of random numbers
    randomPasses = int(input("How many random numbers do you want? "))
    # Loop for user defined number
    for i in range(1,randomPasses + 1):
        randomNumber = random.randint(1,101)
        # Write random numbers to randomNumbers.txt
        outfile.write(str(randomNumber)+'\n')
    outfile.close()
    print('Writing...')
    print('Done.')
        
main()

#########################################################################

# Write another program that reads the random numbers from the file,
# display the numbers, and then display the following data:
# The total of the numbers
# The number of random numbers read from the file

def main():
    infile=open('randomNumbers.txt','r')
    # Define total
    total = 0
    # Define how many numbers are in file
    count = 0
    for line in infile:
        # Remove newwline operator
        line=line.rstrip('\n')
        # Print the random number
        print('Number', count + 1, 'is', line)
        randomNumber = int(line)
        # Add number to total
        total += randomNumber
        count += 1
    infile.close()
    # Print the total of the random numbers
    print('The total of the random numbers is', total)
    # Print how many random numbers are in the file
    print('There are', count,'random numbers in the file.')
    print('Exiting...')


main()