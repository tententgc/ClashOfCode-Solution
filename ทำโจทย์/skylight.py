import math
n = [int(x) for x in input().split()]
z =[int(x) for x in input().split()]
z=z[0]*z[1]
p = int(input())
z*=p
q=0
for i in range(n[0]):
    g =[int(x) for x in input().split()]
    q+=sum(g)
print(math.ceil((z+q)/p))