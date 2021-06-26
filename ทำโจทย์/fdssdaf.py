c = int(input())
e = int(input())
a = 0
b = c
d = 0
if e == 0:
    print(c)
elif e == 1:
    print('IMPOSSIBLE')
elif c == e:
    print(c+1)
else:
    while e*a <= c:
        a += 1
    for i in range(a):
        d = c//e
        c = c-(d*e)
        b += d
        c = c+d
    print(b)
