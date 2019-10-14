def main():
    golfRecord = open('golf.txt', 'r')
    name = golfRecord.readline()
    while name != '':
        score = golfRecord.readline()
        name=name.rstrip('\n')
        score=score.rstrip('\n')
        print(name + ' scored ' + score + ' points')
        name = golfRecord.readline()

    golfRecord.close()

    print('Closing File...')

main()