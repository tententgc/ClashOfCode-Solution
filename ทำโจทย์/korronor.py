import math
a = int(input())
b = int(input())
count=0
for i in range(a,b+1):
    z=math.gcd(a,b)
    print(z)
    l=(i*b)/z
    count*=l
print(count)