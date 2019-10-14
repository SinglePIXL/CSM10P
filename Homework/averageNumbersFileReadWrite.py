def main():
    numbersFile = open('averageNumbers.txt','w')
    # Get five floating point numbers from the user
    for i in range(5):
        print(i + 1, end='. ')
        num = float(input('Enter a number: '))
        # Write numbers to the file
        numbersFile.write(str(num) + '\n')

    numbersFile.close()

    print('Data written...')
    print('Exiting...')

main()


####################################################

def main():
    numbersFile = open("averageNumbers.txt",'r')
    line = numbersFile.readline()
    total = 0
    while line != '':
        num = float(line)
        total += num
        line = numbersFile.readline()
    
    numbersFile.close()
    average = total / 5

    print('The average of the numbers in the file is',(format(average,'.2f')))

main()