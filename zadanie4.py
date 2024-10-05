import math
def calculate (mass,height):
    imt = mass/(height**2)
    return imt

mass = float(input('Введите массу тела в килограммах: '))
height = float(input('Введите рост в метрах: '))

imt = calculate(mass,height)

print(f'Ваш индекс массы тела : {imt}')
if imt < 18.5:
    print('Недостаточная масса тела')
if 18.5 <= imt < 25:
    print('Нормальная масса тела')
if 25 <= imt < 30:
    print('Избыточная масса тела')
else:
    print('Ожирение')

