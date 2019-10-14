def main():
    z=open('numbers.txt','r')
    num1 = int(z.readline())
    int(z.readline())
    num3 = int(z.readline())

    z.close()
    print(num1,num3)

main()