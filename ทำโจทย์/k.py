n, k = [int(i) for i in input().split()]
z = n//k
y = n % k
for i in range(z):
    if i < z:
        print(k, end=" ")
    if i == z-1:
        print(k)
if y > 0:
    print(y)
