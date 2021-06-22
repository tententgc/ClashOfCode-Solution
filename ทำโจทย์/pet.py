c=0
z=0
for i in range(5):
    a = [int(x) for x in input().split()]
    b=sum(a)
    if b>c:
        c=b
        z=i+1
print(z,c)