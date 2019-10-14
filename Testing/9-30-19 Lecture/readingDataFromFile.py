def main():
    infile = open('courses.txt','r')
    file_contents=infile.read()
    infile.close()
    print(file_contents)

main()