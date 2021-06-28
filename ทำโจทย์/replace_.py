a=input()
z=[]
j=1
n=int(input())
for i in range(n):
    c=input()
    z.append(c)
for i in z:
    a=a.replace("_",i,1)
print(a)



