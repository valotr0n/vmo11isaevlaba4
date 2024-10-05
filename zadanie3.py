import math
def calculate (x,y):
    halfSum = (x+y)/2
    dublesum = 2 * x * y

    if x  < y:
        x1 = halfSum
        y1 = dublesum
    else:
        x1 = dublesum
        y1 = halfSum
    return x1, y1

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))

x1 , y1 = calculate(x,y)

print(f'Новое значение x: {x1}',
      f'новое значение y: {y1}')


