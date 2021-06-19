a, b = [int(i) for i in input().split()]
h=[]
n = int(input())
for i in range(n):
    y = int(input())
    h.append(y)
for i in range(n):
    print((h[i]*a)+b)
