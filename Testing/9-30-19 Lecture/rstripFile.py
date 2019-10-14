def main():
    infile = open('courses.txt','r')
    line1=infile.readline()
    line2=infile.readline()
    line3=infile.readline()
    line1=line1.rstrip('\n')
    line2=line2.rstrip('\n')
    line3=line3.rstrip('\n')
    infile.close()
    print('Line one is',line1,'Line two is',line2,'Line 3 is',line3)

main()