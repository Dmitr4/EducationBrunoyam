# Уровень 1

value = (5+(7*5)/8)/3**5
print('значение выражения:', value)

# Уровень 2

v = int(input('Введите скорость байкера: '))
t = int(input('Введите время движения: '))
point = (v*t)%109
print(point)

# Уровень 3

num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
max1 = (num1>num2)*num1+(num2>=num1)*num2
print(max1)