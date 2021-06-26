import math
a= int(input())
b=int(input())
q=a
z=0
y=0
if a==b:
    print (a+1)
if b==1:
    print("IMPOSSIBLE")
if b<=0 or b>a:
    print(a)
else:
    while a >1:
        y+=a%b
        a = a//b
        z+=a
    g=y//b
    if g >0:
        g=g+1   
    print(z+q+g)
