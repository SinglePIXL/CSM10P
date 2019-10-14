def main():
    loopNum = int(input('How many negative numbers would you like to add?'))
    runningTotal = 0
    for i in range(1,loopNum + 1, 2):
        print(i)
        runningTotal += i
    print('The total of the odd numbers is', runningTotal)

main()