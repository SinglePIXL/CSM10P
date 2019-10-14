def main():
    randomNumbersFile = open('randomNumbers.txt','r')
    totalOfNumbers = 0
    line = randomNumbersFile.readline()
    count = 0

    while line != '':
        randomNumber = int(line)
        count += 1
        totalOfNumbers += randomNumber
        print(randomNumber)
        line = randomNumbersFile.readline()
    print(totalOfNumbers)
    print(count)

main()