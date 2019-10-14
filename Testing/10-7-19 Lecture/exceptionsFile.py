try:
    f = open('data.txt')
    f.write('Hello World')
except:
    print('Something went wrong when writing to the file.')

finally:
    f.close()