def total(num):
    num = str(num)
    l = []
    for i in num:
        l.append(int(i))
    s = 0
    for i in l:
        s += i
    return s

n = int(input('Введите целое число: '))
print(total(n))

# можно реализовать через встроенную функцию sum

def amount(num):
    num = str(num)
    l = []
    for i in num:
        l.append(int(i))
    return sum(l)

print(amount(n))