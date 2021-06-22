N = str(input())
a = b = 0
for i in range(len(N)):
    a = ((a * 10) + int(N[i])) % 3
    b = ((b * 10) + int(N[i])) % 11
print(a, b)
