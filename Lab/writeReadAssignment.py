# Two seperate programs for testing creating and writing to a file,
# and reading data from that file seperated by *************

def main():
    outfile = open('courses.txt','w')
    # Write naes of a few courses
    outfile.write('Python prog. \n')
    outfile.write('C++ prog. \n')
    outfile.write('R prog. \n')
    outfile.close()
    print('Data written to file')

main()

**************************************

def main():
    infile = open('courses.txt','r')
    file_contents=infile.read()
    infile.close()
    print(file_contents)

main()