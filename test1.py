import math as m
w,l = [int(x) for x in input().split()] 

n = int(input())
sumValue = 0
for i in range(n):
    x = float(input())
    ans = m.pi * (x**2)
    sumValue += ans

sumValue = w*l - sumValue
if sumValue > 0 and sumValue%1 ==0:
    print(int(sumValue))
elif sumValue<=0:
    print(0)
else:
    print(f"{sumValue:.2f}")