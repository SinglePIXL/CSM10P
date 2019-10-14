# Alec
# numberAnalysisProgram.py
# 10-10-19
# Ver 1.5
# A program that asks the user to enter a series of 20 numbers. 
# The program should store the numbers in a list
# and then display the following data:
# The lowest number in the list
# The highest number in the list
# The total of the numbers in the list
# The average of the numbers in the list

# Set number of numbers required for loop as global
NUM_RANGE = 20
# Import math to find average of the list
import math
def main():
    userNumbers=[0]*NUM_RANGE
    index = 0
    print('Enter a series of', NUM_RANGE, 'numbers')
    # Get as many numbers as in global variable NUM_RANGE
    while index < NUM_RANGE:
        print('Number#',index+1,':',end='')
        # Write the user number to the list
        userNumbers[index] = float(input())
        # Increment index by 1
        index+=1
    # After loop has exited, print the results

    # Lowest number using 'min'
    print('The lowest number in the list is ', end='')    
    print(min(userNumbers))
    # Highest number using 'max'
    print('The highest number in the list is ', end='')
    print(max(userNumbers))
    # Total of the numbers entered into the list
    sumNumbers = sum(userNumbers)
    # The average by dividing the the sumNumbers variable by the NUM_RANGE
    # global
    avgNumbers = sumNumbers / NUM_RANGE
    print('The total of numbers in the list is', sumNumbers)
    print('The average of the numbers in the list is', avgNumbers)

main()