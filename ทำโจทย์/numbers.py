n= int(input())
a = sorted([int(i) for i in input().split()])

for i in range(1,len(a)):
    if a[0]==0:
        a[0],a[i]=a[i],a[0]
print(''.join(a))