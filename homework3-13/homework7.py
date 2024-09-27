from random import randint

n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)]
print(m)

l = []
for i in m:
    max = i[0]
    for j in i:
        if j > max:
            max = j
    l.append(max)

max = l[0]
for i in l:
    if i > max:
        max = i

print(max)
