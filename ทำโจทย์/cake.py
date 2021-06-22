import math
a= int(input())
z=[0,0,0,0,0]
for i in range(a):
    b,c,d,e,f = [int(x) for x in input().split()]
    z[0]+=b*8
    z[1]+=c*6
    z[2]+=d*4
    z[3]+=e*2
    z[4]+=f
q=sum(z)/8
print(math.ceil(q))


