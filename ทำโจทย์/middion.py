def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]


c1 = [[e for e in input().split()] for i in range(int(input()))]
k = list(powerset([e[0] for e in c1]))
kk = list(powerset([e[1] for e in c1]))
sumb = []
sumf = []
nq = []
for i in k:
    f = 0
    for x in i:
        f = f+int(x)
    sumf.append(f*2)
    nq.append(len(c1)-len(i))
for i in kk:
    f = 0
    for x in i:
        f += int(x)
    sumb.append(f)
print(max([((sumb[i]-sumf[i])-(nq[i]**2)) for i in range(len(sumb))]))
