l = [1, 4, 1, 6, 'hello', 'a', 5, 'hello']
n = []
repeat = []

for i in l:
    if i in n:
        if i in repeat:
            repeat
        else:
            repeat.append(i)
    else:
        n.append(i)

print(repeat)

