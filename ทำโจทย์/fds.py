a = input()
j = int(a)
c = 0
for s in a:
    t = int(s)
    c += t
d = []
for i in range(100000):
    b = str(i)
    e=0
    for x in b:
        y = int(x)
        e += y
    if j-i == c+e:
        d.append(i)
print(d[0])
