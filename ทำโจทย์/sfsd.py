n = int(input())
z = 0
for i in input().split():
    x = int(i)
    z += x
if z % a == 0:
    print(int(z/n))
else:
    print(z/n)
