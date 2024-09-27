lst = [56, 9, 11, 2]
lst2 = [3, 81, 5]
# def get_num(l):
s = ''
for i in lst:
    s += str(i)
print(s)
l =[]
for j in s:
    l.append(int(j))

n = (sorted(l))[::-1]

num = ''
for m in n:
    num += str(m)

print(int(num))
