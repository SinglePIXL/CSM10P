def main():
    z=open('numbers.txt','w')
    num1 = int(input('Enter a first number: '))
    num2 = int(input('Enter a second number: '))
    num3 = int(input('Enter a third number: '))

    z.write(str(num1)+'\n')
    z.write(str(num2)+'\n')
    z.write(str(num3)+'\n')
    z.close()
    print('Data written to numbers.txt')

main()