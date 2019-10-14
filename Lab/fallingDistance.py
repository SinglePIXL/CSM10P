# Alec
# fallingDistance.py
# 9-21-19
# Ver 1.3

# Accept an object's falling time in seconds as an argument.
# The function should return the distance in meters that the object has fallen
# during that time interval. Write a program that calls the function in a loop
# that passes the values 1 through 10 as arguments and displays the return
# value

# Display calculation for distance of a falling object
def main():
    # Seconds: Range is 1 second to 10
    for i in range(1,11):
        # Print the calculation
        print('Object has traveled', format (falling_distance(i),',.2f'),\
        'meters per', i, 'second/s.')

# Define variables gravity and distnace
# Time is passed into this function through the timeTraveled arguement
def falling_distance(timeTraveled):
    gravity = 9.8
    distance = 0.5 * gravity * (timeTraveled ** 2)
    return distance


main()