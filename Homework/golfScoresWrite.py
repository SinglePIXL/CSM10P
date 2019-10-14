def playerName():
    nameInput = input('Enter player\'s name: ')
    return nameInput

def main():
    golfRecord = open('golf.txt','w')
    nameLoop = 'y'
    while nameLoop == 'y' or nameLoop == 'Y':
        nameInput = playerName()
        golfRecord.write(str(nameInput) + '\n')
        score = int(input('Enter score for ' + nameInput + ': '))
        golfRecord.write(str(score) + '\n')

        nameLoop = input('Would you like to enter another player? Y/n ' )


    golfRecord.close()
    print('Scores have been recorded in the ledger.')

main()