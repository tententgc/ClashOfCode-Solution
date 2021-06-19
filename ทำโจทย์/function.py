import math
n = int(input())
z = []
if n > 0:
    for i in range(n):
        a = int(input())
        z.append(a)
    z.sort()
    q = z[0]*z[-1]
    y = int(math.sqrt(q))
    print
else:
    print(0)
