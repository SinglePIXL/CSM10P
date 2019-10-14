try:
    print(x)
except:
    print('Invalid data')

finally:
    print("The 'try except' is finished.")
    # closing file will always go in finally