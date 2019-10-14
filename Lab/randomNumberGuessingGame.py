import random

def main():
    number = random.randint(1,101)
    userNum = int(input('Guess the number in the range of 1-100: '))
    startStop = 'y'
    guesses = 0
    while startStop == 'y' or startStop == 'Y':
        if userNum > number:
            userNum = int(input('Too high, try again. '))
            guesses +=1

        elif userNum < number:
            userNum = int(input('Too low, try again. '))
            guesses +=1

        else:
            print('Congratulations!!!')
            guesses +=1
            print('The random number was', number)
            print('You guessed ', guesses, 'times.')
            number = random.randint(1,101)
            guesses = 0

            startStop = input('Would you like to continue? Y/n ')
            if startStop == 'y' or startStop == 'Y':
                userNum = int(input('Guess the number in range of 1-100: '))

            else:
                print('Goodbye')
                exit()





main()