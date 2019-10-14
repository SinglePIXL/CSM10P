try:
    print('Something something something')

except ValueError:
    print('Value Error')

except (ZeroDivisionError,TypeError):
    print('these errors')
except:
    print('All other errors')
    # Handles all other exceptions