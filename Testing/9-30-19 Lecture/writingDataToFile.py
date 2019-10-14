def main():
    outfile = open('courses.txt','w')
    # Write naes of a few courses
    outfile.write('Python prog. \n')
    outfile.write('C++ prog. \n')
    outfile.write('R prog. \n')
    outfile.close()
    print('Data written to file')

main()