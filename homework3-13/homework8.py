d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
print(d)
f ={}

for key, var in d.items():
    f[var] = key

d = f
print(d)
