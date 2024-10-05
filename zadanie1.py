import math
def calculate (x,lambd,R):
    firstcal = (2/math.sqrt(x))
    secondcal = (x-lambd/ R)
    thirdcal = ((((x - lambd/2)**2)**1/3 ) + lambd**2)
    result  = firstcal * (secondcal/thirdcal)
    return result

x = float(input("Введите значение x: "))
lambd = float(input("Введите значение lambd :"))
R = float(input("Введите значение R: "))

result = calculate(x,lambd,R)

print(f'Значение функции: {result}')