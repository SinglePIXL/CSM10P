"""
Alec
temperatureTable.py
9-9-19
Ver 1.2

Display a program that displays a table of the Celsius temperatures 0 through 20
and their Fahrenheit equivalents. 
"""


print('Celcius\t\tFahrenheit')
print('-------------------------')

for celcius in range(21):
    fahrenheit = ((9 / 5) * celcius) + 32
    print(celcius, '\t\t', format(fahrenheit, ',.1f'))