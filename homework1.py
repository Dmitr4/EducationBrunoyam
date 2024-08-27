# # Уровень 1

num1 = int(input('Введите первое целое число: '))
num2 = int(input('Введите второе целое число: '))
num3 = int(input('Введите третье целое число: '))

if num1==num2==num3:
    print(3)
elif (num1!=num2 and num1==num3) or (num1!=num3 and num1==num2):
    print(2)
else:
    print(0)

# Уровень 2

x1 = int(input('Введите номер по вертикали первой клетки (от 1 до 8): '))
y1 = int(input('Введите номер по горизонтали первой клетки (от 1 до 8): '))
x2 = int(input('Введите номер по вертикали второй клетки (от 1 до 8): '))
y2 = int(input('Введите номер по горизонтали второй клетки (от 1 до 8): '))

if x1==x2 or y1==y2:
    print('YES')
else:
    print('NO')

# Уровень 3

password = input('Введите пароль: ')
while True:
    if len(password) > 8 and (password.lower() != password) and (password.upper() != password):
        print('Пароль принят')
        break

    password = input('Введите пароль: ')