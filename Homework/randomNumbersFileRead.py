def main():
    infile=open('randomNumbers.txt','r')
    total = 0
    count = 0
    for line in infile:
        line=line.rstrip('\n')
        print('Number', count + 1, 'is', line)
        randomNumber = int(line)
        total += randomNumber
        count += 1
    infile.close()
    print('The total of the random numbers is', total)
    print('There are', count,'random numbers in the file.')
    print('Exiting...')


main()