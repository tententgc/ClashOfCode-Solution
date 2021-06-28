n = int(input())
y = 0
for i in range(n):
    b = [int(x) for x in input().split()]
    x = b.count(i)
    y += x
print(y)
