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