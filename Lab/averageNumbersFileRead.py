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