"""
Alec
nestedLoop.py
9-9-19
Ver 1.2

Class activity to find the average test scores of students.
"""


numStudents = int(input('Enter number of students: '))
numTestScores = int(input('Enter number of tests scores per student: '))
for student in range(numStudents):
    total = 0.0
    print('Student number', student + 1)
    for testNum in range( numTestScores ):
        print('Test number', testNum +1, end='')
        score = float(input(':'))
        total+= score

    average = total / numTestScores
    print('The average test score number', student +1, 'is ' + "{:.2f}" .format(average))
