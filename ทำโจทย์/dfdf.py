n, m = [int(i) for i in input().split()]
c = 0
s = int(input())
for i in range(n):
    a = input()
    for x in a:
        if x == "o":
            c += s
print(c)
