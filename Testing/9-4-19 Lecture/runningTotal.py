# A running total is a sum of numbers that accumulates with each iteration of a loop
# The variable is used to keep the running total is called an accumulator.

total = 0
for count in range(10):
    num = int(input('Enter a number: '))
    total = total + num     # total is an accumulator

print('Total of ten numbers is', total)