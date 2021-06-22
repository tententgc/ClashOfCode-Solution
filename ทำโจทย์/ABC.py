n = [int(x) for x in input().split()]
a,b,c = sorted(n)
w=input()
for i in w:
    if i=="A":
        print(a,end=' ')
    if i == "B":
        print(b, end=' ')
    if i == "C":
        print(c, end=' ')
