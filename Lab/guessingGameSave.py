import random

def main():
    number = random.randint(1,101)
    userNum = int(input('Guess the number in the range of 1-100'))
    guesses = 0
    while True:
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

            exit()




main()