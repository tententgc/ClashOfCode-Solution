n = int(input())
z = []
y=[]
for i in range(n):
    x = int(input())
    z.append(x)
z.sort()
z.reverse()
for i in z:
    y.append(str(i))
print(" ".join(y))
