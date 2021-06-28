a=int(input())
b=int(input())
c=int(input())
d=int(input())
z=[]
y=[]
for i in range(a+1):
    for j in range(b+1):
        for h in range(c+1):
            z.append([i,j,h])
for i in z:
    if sum(i) !=d:
        y.append(i)
print(y)

