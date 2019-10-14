# Alec
# addNumInRangeFunc.py
# 9-25-19
# Ver 1.3
# A function that accepts an integer value and calculates sum of 
# values from 1 to n(inclusive) and returns the result
# back to the place we call it.

def myfunc(n):
    count = 0
    for i in range(1, n +1):
        count+= i

    return count

def main():
    sumOf = int(input('Enter a number: '))
    print(myfunc(sumOf))

main()