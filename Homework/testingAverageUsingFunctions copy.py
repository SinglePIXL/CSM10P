# Alec
# testingAverageUsingFunctions.py
# 9/16/19
# Version 1.12

# A program that asks the user to enter five test scores. 
# The program should display a letter grade for each score 
# and the average test score


def calc_average():
    total = 0
    for grade in range(1,6):
        print('Test number', grade, end='')
        testScore = int(input(': '))
        if testScore > 100 or testScore < 0:
            print('Invalid test score. Please enter a number greater than 0 ' \
            'and less than 101 for grade',grade, end='')
            testScore = int(input(': '))
            determine_grade(testScore)

        total+= testScore

    average = total / 5
    print('Final grade: ', end='')
    determine_grade(average)

    


def determine_grade(testScore):
    if testScore <= 100 and testScore >= 90:
        print('Your score of ', testScore, 'is an A!')
    
    elif testScore <= 89.9 and testScore >= 80:
        print('Your score of ', testScore, 'is a B.')

    elif testScore <= 79.9 and testScore >= 70:
        print('Your score of ', testScore, 'is a C')

    elif testScore <= 69.9 and testScore >= 70:
        print('Your score of ', testScore, 'is a D')

    else:
        print('Your score of', testScore, 'is an F')


calc_average()