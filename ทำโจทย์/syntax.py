a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
a.sort()
b.sort()
if (a[1]<b[0]):
    print("NONE")
else:
    print(a[1]-b[0])