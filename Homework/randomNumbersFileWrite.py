

# A program that writes a series of random numbers to a file.
# Each random number should be in the range of 1 through 100.
# The user specifies how many random numbers the file will hold.

import random

def main():
    outfile = open('randomNumbers.txt','w')
    randomPasses = int(input("How many random numbers do you want? "))
    for i in range(1,randomPasses + 1):
        randomNumber = random.randint(1,101)
        outfile.write(str(randomNumber)+'\n')
    outfile.close()
    print('Writing...')
    print('Done.')
        
main()

