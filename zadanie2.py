import math

def calculate(x):
    areaSqura = x**2
    areaCircle = math.pi * ((x/2)**2)
    lastArea = areaSqura - areaCircle
    return lastArea

x = float(input('Введите значение x: '))
print('Значение должно быть положительным')
lastArea = calculate(x)
print(f'Разница между S квадрата и S вписанного круга = {lastArea}')
