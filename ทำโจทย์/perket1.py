n=int(input())
a=[]
for i in range(n):
    b=input().split()
    a.append(b)
minn=2e9
for i in range(1,pow(2,n),1):
    s=1
    b=0
    use=[]
    z=i
    while(z!=0):
        use.append(z%2)
        z//=2
    while(len(use)!=n):
        use.append(0)
    use.reverse()
    for j in range(0,n,1):
        if(use[j]==1):
            s*=int(a[j][0])
            b+=int(a[j][1])
    minn=min(minn,abs(s-b))
print(min)