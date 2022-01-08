a,b,int(c)=input().split(" ")
l=len(a)
for i in range(c*2+1):print(f'{b*c} {a} {b*c}'if i==c else b*(c*2+l+2))