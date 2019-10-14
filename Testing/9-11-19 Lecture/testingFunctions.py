def main():
    n = int(input('Enter number'))
    sum = add_odds(n)
    print('the value is', sum)
def add_odds(n):
    sum = 0
    for i in range (1, n + 1, 2):
        sum += i

main()