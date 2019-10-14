import random

MIN = 1
MAX = 6

def main():
    reRoll = 'y'
    while reRoll == 'y' or reRoll == 'Y':
        print(random.randint(MIN,MAX))
        reRoll = input('Would you like to reroll? Y/n ')

main()