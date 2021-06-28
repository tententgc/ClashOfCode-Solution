n = int(input())
z=set()
a= [int(x) for x in input().split()]
for i in a:
    z.add(i)
y=list(z)
y.sort()
print(y[-2])