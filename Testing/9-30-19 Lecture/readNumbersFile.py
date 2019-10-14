def main():
    z=open('numbers.txt','r')
    num1 = int(z.readline())
    num2 = int(z.readline())
    num3 = int(z.readline())

    z.close()
    total = num1 + num2 + num3
    print('The total is ',total)

main()