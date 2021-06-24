a=int(input())
n=[int(x) for x in input().split()]
d=dict()
for i in n:
    if i in d:d[i]+=1
    else:d[i]=1
m =max([x for x in d.values()])
for x in sorted(d):
    if m== d[x]:print(x,end=" ")