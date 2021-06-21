a = [int(x) for x in input().split()]
z = 0
for i in a:
    if i%2==0:
        z += i
    else:
        z -= i
print(z)
