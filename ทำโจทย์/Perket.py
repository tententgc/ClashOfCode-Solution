import itertools
n = int(input())
m = set()
l = [[int(e) for e in input().split()] for i in range(n)]
for i in range(n):
    for j in itertools.combinations(l, i+1):
        s, b = 1, 0
        for si, bi in j:
            s *= si
            b += bi
        m.add(abs(s-b))
print(min(m))
