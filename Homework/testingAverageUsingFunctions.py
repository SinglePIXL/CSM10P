# Alec
# testingAverageUsingFunctions.py
# 9/13/19
# Version 1.6

# A program that asks the user to enter five test scores. 
# The program should display a letter grade for each score 
# and the average test score


def calc_average():
    total = 0
    for grade in range(1,6):
        print('Test number', grade, end='')
        testScore = int(input(': '))
        determine_grade(testScore)

        total+= testScore

    average = total / 5
    determine_total_grade(average)

    


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
        print('Your score of ', testScore, 'is an F')

def determine_total_grade(average):
    
    if average <= 100 and average >= 90:
        print('Your final test score of ', average, 'is an A!')
    
    elif average <= 89.9 and average >= 80:
        print('Your final test score of ', average, 'is a B.')

    elif average <= 79.9 and average >= 70:
        print('Your final test score of ', average, 'is a C')

    elif average <= 69.9 and average >= 70:
        print('Your final test score of ', average, 'is a D')

    else:
        print('Your final test score of ', average, 'is an F')




calc_average()