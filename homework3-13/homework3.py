x = float(input('Сумма начального вклада в рублях: '))
y = float(input('Сумма окончательного вклада в рублях: '))
p = float(input('Процент по вкладу: '))
p = p/100 + 1
t = 0
while x <= y:
    x *= p
    x = int(x)
    print(x)
    t += 1
print(f'{t} лет/года')

