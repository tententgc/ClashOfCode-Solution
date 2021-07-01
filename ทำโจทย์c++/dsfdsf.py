n = int(input())
z = []
for i in range(n):
    b = [int(x) for x in input().split()]
    b.sort()
    print(b[-2])
